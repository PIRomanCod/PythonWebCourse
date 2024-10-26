from pathlib import Path


IMAGE = []
VIDEO = []
DOCS = []
AUDIO = []
ARCHIVE = []
MY_OTHER = []


REGISTER_EXTENSIONS = {
    'JPEG': IMAGE, 'JPG': IMAGE, 'SVG': IMAGE, 'PNG': IMAGE,
    'AVI' : VIDEO, 'MP4':VIDEO, 'MOV' : VIDEO, 'MKV': VIDEO,
    'DOC': DOCS, 'DOCX': DOCS, 'TXT': DOCS, 'PDF': DOCS, 'XLSX': DOCS, 'PPTX': DOCS,
    'MP3': AUDIO, 'OGG': AUDIO, 'WAV': AUDIO, 'AMR': AUDIO,
    'ZIP': ARCHIVE, 'GZ': ARCHIVE, 'TAR': ARCHIVE, 'RAR': ARCHIVE,
}

FOLDERS = []
EXTENSIONS = set()
UNKNOWN = set()


def get_extension(filename: str) -> str:
    return Path(filename).suffix[1:].upper()


def scan(folder: Path) -> None:
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in ('Archives', 'Video', 'Audio', 'Documents', 'Images', 'MY_OTHER'):
                FOLDERS.append(item)
                scan(item)
            continue


        ext = get_extension(item.name)
        fullname = folder / item.name
        if not ext:
            MY_OTHER.append(fullname)
        else:
            try:
                container = REGISTER_EXTENSIONS[ext]
                EXTENSIONS.add(ext)
                container.append(fullname)
            except KeyError:
                UNKNOWN.add(ext)
                MY_OTHER.append(fullname)

def handle_media(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / filename.name)


def handle_other(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / filename.name)


def handle_folder(folder: Path):
    try:
        folder.rmdir()
    except OSError:
        None


def sort(folder: Path):
    scan(folder)
    for file in IMAGE:
        handle_media(file, folder / 'Image')
    for file in VIDEO:
        handle_media(file, folder / 'Video')
    for file in DOCS:
        handle_media(file, folder / 'Docs')
    for file in AUDIO:
        handle_media(file, folder / 'Audio')

    for file in MY_OTHER:
        handle_other(file, folder / 'Other')
    for file in ARCHIVE:
        handle_media(file, folder / 'Archives')
    for folder in FOLDERS[::-1]:
        handle_folder(folder)


def start(string):
    folder_for_scan = Path(string)
    sort(folder_for_scan)



