from models import Notes, Record, Tag
import connect


def simple_output():
    notes = Notes.objects()
    for note in notes:
        print("-------------------")
        records = [f'description: {record.description}, done: {record.done}' for record in note.records]
        tags = [tag.name for tag in note.tags]
        print(f"id: {note.id} name: {note.name} date: {note.created} records: {records} tags: {tags}")


def dict_output():
    notes = Notes.objects()
    print("-------------------")
    for note in notes:
        print(note.to_mongo().to_dict())


def tags_output(tags__name):
    notes = Notes.objects(tags__name=tags__name)
    for note in notes:
        records = [f'description: {record.description}, done: {record.done}' for record in note.records]
        tags = [tag.name for tag in note.tags]
        print(f"id: {note.id} name: {note.name} date: {note.created} records: {records} tags: {tags}")


def some_tags_output(tags):
    notes = Notes.objects(tags__name__in=tags)
    for note in notes:
        records = [f'description: {record.description}, done: {record.done}' for record in note.records]
        tags = [tag.name for tag in note.tags]
        print(f"id: {note.id} name: {note.name} date: {note.created} records: {records} tags: {tags}")


def note_update(_id, name):
    _id = _id
    note = Notes.objects(id=_id)
    note.update(name=name)
    return note


def note_delete(_id):
    note = Notes.objects(id=_id).delete()
    return note


if __name__ == '__main__':
    # simple_output()
    dict_output()
    # tags_output('Purchases')
    # some_tags_output(['Fun', 'Purchases'])
    # note_update("6401f148b3b0d802595e6637", "Shopping moll")
    # note_delete("6401f148b3b0d802595e6638")



