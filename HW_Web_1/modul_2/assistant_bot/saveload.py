import pickle
from pathlib import Path
import os


class FileStorage():
    def load_file(self):
        try:
            with open(Path.home().joinpath('PersonalAssistant').joinpath('AddressBookData.bin'), 'rb') as l_file:
                self.data = pickle.load(l_file)
        except FileNotFoundError:
            if not os.path.exists(Path.home().joinpath('PersonalAssistant')):
                os.makedirs(Path.home().joinpath('PersonalAssistant'))
            with open(Path.home().joinpath('PersonalAssistant').joinpath('AddressBookData.bin'), 'w') as f:
                pass
            self.data = {}

    def save_file(self):
        with open(Path.home().joinpath('PersonalAssistant').joinpath('AddressBookData.bin'), 'wb') as s_file:
            pickle.dump(self.data, s_file)
