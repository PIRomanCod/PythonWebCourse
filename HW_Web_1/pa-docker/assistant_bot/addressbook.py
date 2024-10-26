from collections import UserDict
from saveload import FileStorage
import pickle
import record


class AddressBook(UserDict, FileStorage):
    def __init__(self):
        super().__init__()
        self.load_file()

    def add_record(self, record):
        self.data[record.name.value] = record

    def delete_contact(self, name: str):
        del self.data[name]

    def get_contact(self, name: str):
        if name in self.data:
            contact_info = []
            email_info = ""
            address_list = ""
            notes_string = ""
            birthday = ""
            phones_list = ', '.join(
                [phone.value for phone in self.data[name].phones])
            contact_info.append(f"Phones: {phones_list}")
            if self.data[name].birthday:
                birthday = self.data[name].birthday.value
                contact_info.append(f"Burned: {birthday}")
            if self.data[name].email:
                email_info = self.data[name].email.value
                contact_info.append(f"Email: {self.data[name].email.value}")

            if self.data[name].notes:
                notes_list = []
                string_tags = ""
                for text, tags in self.data[name].notes.items():
                    if tags:
                        string_tags = ", ".join(tags)
                    notes_list.append(f"{text}, #{string_tags}")
                notes_string = "; ".join(notes_list)
                contact_info.append(f"Notes: {notes_string}")
            if self.data[name].address:
                address_list = self.data[name].address.value
                contact_info.append(f"Lives: {address_list.title()}")

            # return f"Contact - {name.capitalize()} have next information: {[item for item in contact_info]}"
            return f"{name.capitalize()} | {phones_list} | {birthday} | {email_info} | {notes_string} | {address_list.title()}"

            # return f"{name.capitalize()} have next information: {[item for item in contact_info]}"
        return f"There is no contacts with this data"

    def find_text(self, text: str):
        search_list = []
        for key, value in self.data.items():
            if value.notes:
                for note, tags in value.notes.items():
                    if note.find(text) != -1:
                        search_list.append(f"{key.title()}: {note}, #{tags}")
        if len(search_list) > 0:
            return search_list
        else:
            return f"There is no contacts with this data"

    def find_tag(self, tag: str):
        search_list = []
        for key, value in self.data.items():
            if value.notes:
                for note, tags in value.notes.items():
                    if tag in tags:
                        search_list.append(f"{key.title()}: {note}, #{tags}")
        if search_list:
            return search_list
        else:
            return f"There is no contacts with this data"

    def search_contacts(self, name: str):
        search_list = []
        for key, value in self.data.items():
            if name in key:
                search_list.append(self.get_contact(key))
            elif name in value.get_info():
                search_list.append(self.get_contact(key))
        if len(search_list) > 0:
            return search_list
        return f"There is no contacts with this data"

    def iterator(self, count=5):
        contact_list = []
        for contact in self.data.values():
            contact_list.append(contact)
            if len(contact_list) == count:
                yield contact_list
                contact_list = []
        if contact_list:
            yield contact_list

    def get_birthdays(self, timedelta: int):
        self.list_birthdays = {}
        for item in self.data:
            if isinstance(self.data[item].day_to_birthday(), int) and self.data[item].day_to_birthday() <= int(
                    timedelta):
                self.list_birthdays.update(
                    {self.data[item].day_to_birthday(): item.capitalize()})
        self.list_birthdays = sorted(self.list_birthdays.items())
        return self.list_birthdays
