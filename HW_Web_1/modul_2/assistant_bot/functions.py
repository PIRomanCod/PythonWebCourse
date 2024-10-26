from addressbook import AddressBook
from input_error import input_error
from record import Record
from exc import NoUserError, NoteExistError
import cleaner
from abs_interface import UserOutput


def parser(user_input: str):
    parsed_input = user_input.lower().strip().split()
    return handler(parsed_input)


@input_error
def handler(parsed_input: str):
    if parsed_input[0] in commands_dict:
        if len(parsed_input) == 1:
            action = commands_dict.get(parsed_input[0])()
        else:
            action = commands_dict.get(parsed_input[0])(
                (" ").join(parsed_input[1:]))
    else:
        raise KeyError
    return action


def hello():
    return f"How can I help you? Enter: 'help' for manual"


# try to refactoring of spliter
def separator(string):
    pass
    # elements_list = string.split()


def add(string: str):
    new_elem = string.split()
    if users.data.get(new_elem[0]):
        return "Contact already exist"
    searching_result = search(new_elem[1])
    if new_elem[1] in searching_result:
        return f"The phone number already exist for contact: '{searching_result.split()[2]}'"
    record = Record(new_elem[0])
    record.add_phone(new_elem[1])
    users.add_record(record)
    return f"You added new contact: {new_elem[0].capitalize()} with phone number: {new_elem[1]}"


def add_phone(string: str):
    new_elem = string.split()
    if users.data.get(new_elem[0]):
        searching_result = search(new_elem[1])
        if new_elem[1] in searching_result:
            return f"The phone number already exist for contact: '{searching_result.split()[2]}'"
        record = users.data[new_elem[0]]
        record.add_phone(new_elem[1])
        return f"You added contact {new_elem[0]} with number {new_elem[1]}"
    else:
        return "There is no contact with this name"


def add_note(string: str):
    list_elem = string.split('#')
    hashtag = list_elem[1:]
    hashtag_clear = [item.strip() for item in hashtag]
    new_elem = list_elem[0].split()
    name = new_elem[0]
    text = " ".join(new_elem[1:])
    if users.data.get(name):
        if users.data[name].notes.get(text):
            raise NoteExistError
        record = users.data[name]
        record.add_note(text, hashtag_clear)
        users.add_record(record)
        return f"Note: '{text}' with tag: {hashtag_clear} added to contact {name.title()}."
    else:
        return "There is no contact with this name."


def change_attr(string: str):
    new_elem = string.split()
    if new_elem[0] not in users.data:
        raise NoUserError
    else:
        record = users.data[new_elem[0]]
        if new_elem[1] in ["phones", "note", "birthday", "email", "address"]:
            if new_elem[1] == "phones":
                if len(new_elem) < 4:
                    return "The command need more args"
                if new_elem[2] == new_elem[3]:
                    return f"Phones are equal"
                if record.change_phones(new_elem[2], new_elem[3]) is True:
                    return f"{new_elem[0].title()}'s phone changed from {new_elem[2]} to {new_elem[3]}"
                else:
                    return "Phone not found"

            elif new_elem[1] == "note":
                string_note = (" ").join(new_elem[2:])
                if string_note.find("->") == -1:
                    return "Separator '->' not found"
                result = record.change_note(string_note)
                if result is True:
                    return f"Set {new_elem[0].title()}'s note: {string_note}"
                elif result == "ManyMatch":
                    return f"Too many matches in {new_elem[0].title()}'s notes"
                elif result == "MatchNotFound":
                    return f"Not match found in {new_elem[0].title()}'s notes"
                elif result == "NoteNotFound":
                    return f"Notes not found in {new_elem[0].title()}'s notes"

            elif new_elem[1] == "birthday":
                if len(new_elem) < 3:
                    return "The command need more args"
                if record.change_birthday(new_elem[2]) is True:
                    return f"Set {new_elem[0].title()}'s birthday to {new_elem[2]}"

            elif new_elem[1] == "email":
                if len(new_elem) < 3:
                    return "The command need more args"
                if record.change_email(new_elem[2]) is True:
                    return f"Set {new_elem[0].title()}'s email to {new_elem[2]}"

            elif new_elem[1] == "address":
                string_address = (" ").join(new_elem[2:])
                if len(new_elem) < 3:
                    return "The command need more args"
                if record.change_address(string_address) is True:
                    return f"Set {new_elem[0].title()}'s address to {string_address.title()}"

        else:
            return "Attribute doesn't exist"


def delete_attribute(string: str):
    new_elem = string.split()
    if new_elem[0] not in users.data:
        raise NoUserError
    else:
        record = users.data[new_elem[0]]
        if new_elem[1] in ["phones", "birthday", "email", "note", "notes", "address"]:
            if new_elem[1] == "phones":
                if len(new_elem) < 3:
                    return "The command need more args"
                if record.delete_attribute(new_elem[1], new_elem[2]) is True:
                    return f"{new_elem[0].title()}'s phone {new_elem[2]} deleted"
                else:
                    return "Phone not found"

            elif new_elem[1] == "notes":
                if len(new_elem) < 3:
                    return "The command need more args"
                result = record.delete_attribute(new_elem[1], (" ").join(new_elem[2:]))
                if result is True:
                    return f"Deleted all {new_elem[0].title()}'s notes"
                elif result is False:
                    return "Input 'notes all' if you want to delete all notes"
                else:
                    return "Notes not found"

            elif new_elem[1] == "note":
                if len(new_elem) < 3:
                    return "The command need more args"
                string_note = " ".join(new_elem[2:])
                result = record.delete_attribute(new_elem[1], string_note)
                if result is True:
                    return f"Deleted {new_elem[0].title()}'s note: {string_note}"
                elif result == "ManyMatch":
                    return f"Too many matches in {new_elem[0].title()}'s notes"
                elif result == "MatchNotFound":
                    return f"Not match found in {new_elem[0].title()}'s notes"
                elif result == "NoteNotFound":
                    return f"Notes not found in {new_elem[0].title()}'s notes"

            elif new_elem[1] == "birthday":
                if record.delete_attribute(new_elem[1]) is True:
                    return f"Deleted {new_elem[0].title()}'s birthday"
                else:
                    return f"{new_elem[0].title()}'s birthday not found"

            elif new_elem[1] == "email":
                if record.delete_attribute(new_elem[1]) is True:
                    return f"Deleted {new_elem[0].title()}'s email"
                else:
                    return f"{new_elem[0].title()}'s email not found"

            elif new_elem[1] == "address":
                if record.delete_attribute(new_elem[1]) is True:
                    return f"Deleted {new_elem[0].title()}'s address"
                else:
                    return f"{new_elem[0].title()}'s address not found"
        else:
            return "Attribute doesn't exist"


def find_tag(string: str):
    new_elem = string.split()
    if new_elem[0]:
        string_result = ""
        result = users.find_tag(new_elem[0])
        if type(result) == list:
            string_result = "\n".join(result)
        else:
            string_result = result
        return string_result
    else:
        return "The command need more args"


def find_text(string: str):
    if string:
        string_result = ""
        result = users.find_text(string)
        if type(result) == list:
            string_result = "\n".join(result)
        else:
            string_result = result
        return string_result
    else:
        return "The command need more args"


def search(string: str):
    new_elem = string.split()
    result = users.search_contacts(new_elem[0])
    if type(result) == list:
        result = '\n'.join(result)
    # res = UserOutput(result)
    # return res.get_table()
    return result


def show_all():
    if not users.data:
        return "AddressBook is empty"
    result = [record.get_info() for page in users.iterator()
              for record in page]
    #return '\n'.join(result)
    res = UserOutput(result)
    return res.get_table()

def search_info(string: str):
    result = [record.get_info() for page in users.iterator()
              for record in page]
    output = []
    for item in result:
        if string in item:
            output.append(item)
    res = UserOutput(output)
    return res.get_table()


def delete_contact(string: str):
    new_elem = string.split()
    users.delete_contact(new_elem[0])
    return f"You delete contact {new_elem[0]}"


def days_to_birthday(string: str):
    new_elem = string.split()
    record = users[new_elem[0]]
    return f" Contact {string} has {record.day_to_birthday()} till his Birthday"


def birthday_list(timedelta: int):
    after = []
    for i in users.get_birthdays(timedelta):
        a, b = i
        after.append("-" * 35)
        after.append(str(a) + " days | till " + b + "'s Birthday |")
    return '\n'.join(after)


def sort_files(string: str):
    cleaner.start(string)
    return f" Files in {string} have been sorted"


def stop():
    return "Good bye!"


def manual():
    return '''Please enter one of the commands:
    >>help,
    >>add_contact 'name' 'number (3 operator and 7 numbers digit)',
    >>add_phone 'name' 'number (3 operator and 7 numbers digit)',
    >>add_note: 'name'(or 'unnamed') 'the note text' '#hashtag' '#hashtag'...
    >>search_info 'name' or 'part of info',
    >>edit 'name' 'phone'  'new_value', 
                  'note' 'start with.. - change if only one match found'  
                          '->' 'new text' (hashtag stay the same)
                  'birthday' 'new_value',
                  'email' 'new_value',
                  'address' 'new_value'   
    >>delete_info 'name' 'phone' 'value',
                         'note' 'start with..' - delete if only one match found
                         'notes' 'all'  - delete all notes
                         'birthday' 
                         'email' 
                         'address' 

    >>delete_contact 'name',
    >>days_to_birthday 'name',
    >>find_tag 'tag'
    >>find_text 'text'
    >>birthday_list 'period days',
    >>show_all",
    >>sort, 'path to folder' (full path to folder which needs to be sorted),
    >>exit, >>good_bye, >>close
    '''


commands_dict = {"hello": hello,
                 "help": manual,
                 "add_contact": add,
                 "add_phone": add_phone,
                 "add_note": add_note,
                 "edit": change_attr,
                 "search": search,
                 "delete_info": delete_attribute,
                 "delete_contact": delete_contact,
                 "days_to_birthday": days_to_birthday,
                 "find_tag": find_tag,
                 "find_text": find_text,
                 "birthday_list": birthday_list,
                 "show_all": show_all,
                 "search_info" : search_info,
                 "sort": sort_files,
                 "exit": stop}

users = AddressBook()
