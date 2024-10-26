'''ДЗ 9:
CLI (Command Line Interface)
3 частини:
-Парсер команд.
-Функції обробники команд — набір функцій, які ще називають handler
-Цикл запит-відповідь. Ця частина програми відповідає за отримання від користувача даних та повернення користувачеві відповіді від функції-handlerа
Функціонал:
- бот-асистент повинен вміти зберігати ім'я та номер телефону,
- знаходити номер телефону за ім'ям,
- змінювати записаний номер телефону,
- виводити в консоль всі записи, які зберіг
Всі помилки введення повинні оброблятися за допомогою декоратора input_error, повідомлення користувачеві про помилки

Додаткове розширення у ДЗ 10:
В цій домашній роботі ви повинні реалізувати такі класи:
-Клас AddressBook, який успадковується від UserDict, та ми потім додамо логіку пошуку за записами до цього класу.
-Клас Record, який відповідає за логіку додавання/видалення/редагування необов'язкових полів та зберігання обов'язкового поля Name.
-Клас Field, який буде батьківським для всіх полів, у ньому потім реалізуємо логіку загальну для всіх полів.
-Клас Name, обов'язкове поле з ім'ям.
-Клас Phone, необов'язкове поле з телефоном та таких один запис (Record) може містити кілька.
- Реалізовано всі класи із завдання.
- Записи Record у AddressBook зберігаються як значення у словнику. В якості ключів використовується значення Record.name.value.
- Record зберігає об'єкт Name в окремому атрибуті.
- Record зберігає список об'єктів Phone в окремому атрибуті.
- Record реалізує методи для додавання/видалення/редагування об'єктів Phone.
- AddressBook реалізує метод add_record, який додає Record у self.data.


Додаткове розширення у ДЗ 11:
-Додамо поле для дня народження Birthday, може бути тільки одне.
-Додамо функціонал роботи з Birthday у клас Record, а саме функцію days_to_birthday, яка повертає кількість днів до наступного дня народження.
- Додамо функціонал перевірки на правильність наведених значень для полів Phone, Birthday.
- Додамо пагінацію (посторінковий висновок) для AddressBook для ситуацій, коли книга дуже велика і треба показати вміст частинами, а не все одразу.
    Реалізуємо це через створення ітератора за записами.
- AddressBook реалізує метод iterator, який повертає генератор за записами AddressBook і за одну ітерацію повертає уявлення для N записів.
- Клас Record приймає ще один додатковий (опціональний) аргумент класу Birthday
- Клас Record реалізує метод days_to_birthday, який повертає кількість днів до наступного дня народження контакту, якщо день народження заданий.
- setter та getter логіку для атрибутів value спадкоємців Field.
- Перевірку на коректність веденого номера телефону setter для value класу Phone.
- Перевірку на коректність веденого дня народження setter для value класу Birthday.

Додаткове розширення у ДЗ 12:
- Додати функціонал збереження адресної книги на диск та відновлення з диска.
- Додати користувачеві можливість пошуку вмісту книги контактів, щоб можна було знайти всю інформацію про одного або кількох користувачів за кількома цифрами номера телефону або літерами імені

Додаткове розширення у WEB ДЗ 2:
- Намалюйте UML діаграму вашого курсового застосунку "Персональний помічник".
- Застосунок потрібно розвивати і частиною застосунку, що найчастіше змінюється, зазвичай, є інтерфейс користувача (консоль поки що). 
    Модифікуйте код вашого застосунку, щоб представлення інформації користувачеві 
    (виведення карток з контактами користувача, нотатками, сторінка з інформацією про доступні команди) було легко змінити. 
    Для цього треба описати абстрактний базовий клас для представлень користувача і конкретні реалізації, 
    які наслідують базовий клас і реалізують консольний інтерфейс.
'''

from abc import ABC, abstractmethod
from datetime import datetime, date
import pickle
import re
from collections import UserDict


class VerificationError(Exception):
    pass


class EmailVerificationError(Exception):
    pass


class OwnerError(Exception):
    pass


class NoUserError(Exception):
    pass


def input_error(func):
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except TypeError:
            return "The command don't need args"
        except IndexError:
            return "The command need more args"
        except KeyError:
            return "The command is unknown"
        except VerificationError:
            return "The phone number incorrect 3 + 7 phone digits. Try again!"
        except EmailVerificationError:
            return EmailVerificationError("Email is not valid. Try again!")
        except OwnerError:
            return "The phone number is related with other contact"
        except NoUserError:
            return "AddressBook hasn't the contact name yet, please add before change"
        except ValueError:
            return "Something goes wrong. Input 'help' for manual"

    return inner


class Field:
    def __init__(self, value: str) -> str:
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def __str__(self):
        return self.value

    def __repr__(self):
        return f'{self.value}'


class Name(Field):

    @Field.value.setter
    def value(self, value):
        if value.isdigit():
            raise ValueError("Name cannot be a numbers")
        self._value = value


class Phone(Field):
    @Field.value.setter
    def value(self, phone):
        if phone.isdigit() and len(phone) == 10:
            self._value = phone
        else:
            raise VerificationError


class Email(Field):

    @Field.value.setter
    def value(self, email):
        regex = re.compile(
            r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if re.fullmatch(regex, email):
            self._value = email
        else:
            raise EmailVerificationError("Email is not valid")


class Notes(UserDict):
    pass


class Address(Field):
    pass


class Birthday(Field):

    @Field.value.setter
    def value(self, b_day: str) -> date:
        current_date = datetime.now().date()
        b_day_date = datetime.strptime(b_day, '%d/%m/%Y').date()
        if b_day_date > current_date:
            raise ValueError("You entered date that earlier current date")
        self._value = b_day


class AddressBook(UserDict):
    def __init__(self):
        super().__init__()
        self.load_file()

    def add_record(self, record):
        self.data[record.name.value] = record

    def delete_contact(self, name):
        del self.data[name]

    def get_contact(self, name):
        if name in self.data:
            contact_info = []
            phones_list = ', '.join(
                [phone.value for phone in self.data[name].phones])
            contact_info.append(f"Phones: {phones_list}")
            if self.data[name].b_day:
                b_day = self.data[name].b_day.value
                contact_info.append(f"Burned: {b_day}")
            if self.data[name].email:
                contact_info.append(f"Email: {self.data[name].email.value}")
            if self.data[name].notes:
                notes_list = self.data[name].notes
                contact_info.append(f"Notes: {notes_list}")
            if self.data[name].address:
                address_list = self.data[name].address.value
                contact_info.append(f"Lives: {address_list.capitalize()}")

            return f"Contact - {name.capitalize()} have next information: {[item for item in contact_info]}"
        else:
            return f"There is no contacts with this data"

    def search_contacts(self, name):
        search_list = []
        for key, value in self.data.items():
            if name in key:
                search_list.append(self.get_contact(key))
            elif name in value.get_info():
                search_list.append(self.get_contact(key))

        if len(search_list) > 0:
            return f"I found: {', '.join(search_list)}"
        else:
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

    def save_file(self):
        with open('AddressBookData.bin', 'wb') as s_file:
            pickle.dump(self.data, s_file)

    def load_file(self):
        try:
            with open('AddressBookData.bin', 'rb') as l_file:
                self.data = pickle.load(l_file)
        except FileNotFoundError:
            pass


class Record(Field):
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.b_day = None
        self.email = None
        self.notes = {}
        self.address = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def change_attr(self, attribute, old_value=None, new_value=None):
        if attribute not in ["name", "phones", "b_day", "email", "notes", "address"]:
            raise IndexError("You didn't write an attribute")
        self.attribute = getattr(self, attribute)
        if attribute == "phones":
            for item in self.phones:
                if item.value == old_value:
                    if new_value not in self.phones:
                        item.value = new_value
                        return True
        elif attribute == "notes":
            self.notes[old_value] = new_value
            return True
        elif attribute == "b_day":
            self.b_day = Birthday(new_value)
            return True
        elif attribute == "address":
            self.address = Address(new_value)
            return True
        elif attribute == "email":
            self.email = Email(new_value)
            return True

    def delete_attribute(self, attribute, item=None):
        if attribute == "phones":
            for phone in self.phones:
                if phone.value == item:
                    self.phones.remove(phone)
                    return True
        elif attribute == "notes":
            try:
                if self.notes[item]:
                    self.notes.pop(item, "There is not such notes")
                    return True
            except KeyError:
                return "There is not such notes"
        elif attribute == "b_day":
            self.b_day = None
            return True
        elif attribute == "address":
            self.address = None
            return True
        elif attribute == "email":
            self.email = None
            return True

    def get_info(self):
        b_day_info = ''
        email_info = ''
        notes_info = ''
        address_info = ''
        phones_info = [phone.value for phone in self.phones]

        if self.b_day:
            b_day_info = f'Burned: {self.b_day.value}'
        if self.email:
            email_info = f'Email: {self.email.value}'
        if self.notes:
            notes_info = f'Notes: {self.notes}'
        if self.address:
            address_info = f'Lives: {self.address.value.capitalize()}'
        return f"Contact - {self.name.value.capitalize()} : {', '.join(phones_info)} {b_day_info} {email_info} {notes_info} {address_info}"

    def add_b_day(self, date):
        self.b_day = Birthday(date)

    def day_to_b_day(self):
        if not self.b_day:
            raise ValueError("The contact's birthday date not defined yet")

        current_date = datetime.now().date()
        b_day_date = datetime.strptime(
            self.b_day.value, '%d/%m/%Y').date()
        new_date_for_b_day = b_day_date.replace(year=current_date.year)

        if new_date_for_b_day < current_date:
            new_date_for_b_day = new_date_for_b_day.replace(
                year=current_date.year + 1)
        return (new_date_for_b_day - current_date).days

    def add_notes(self, note):
        self.notes.update(note)

    def add_address(self, address):
        self.address = Address(address)

    def add_email(self, email):
        self.email = Email(email)

    def __str__(self):
        return f'{self.name, self.phones, self.b_day, self.email, self.notes, self.address}'

    def __repr__(self):
        return f'{self.name, self.phones, self.b_day, self.email, self.notes, self.address}'


def parser(user_input):
    parsed_input = user_input.lower().strip().split()
    return handler(parsed_input)


@input_error
def handler(parsed_input):
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


def add(string):
    new_elem = string.split()
    if users.data.get(new_elem[0]):
        return "Contact already exist"

    record = Record(new_elem[0])
    record.add_phone(new_elem[1])
    users.add_record(record)
    return f"You added new contact: {new_elem[0]} with phone number: {new_elem[1]}"


def add_phone(string):
    new_elem = string.split()
    if users.data.get(new_elem[0]):
        record = users.data[new_elem[0]]
        record.add_phone(new_elem[1])
        return f"You added contact {new_elem[0]} with number {new_elem[1]}"
    else:
        return "There is no contact with this name"


def change_attr(string):
    new_elem = string.split()
    if new_elem[0] not in users.data:
        raise NoUserError
    else:
        record = users.data[new_elem[0]]
        if record.change_attr(new_elem[1], new_elem[2], (" ").join(new_elem[3:])) is True:
            return f"You changed for contact {new_elem[0].capitalize()} attribute {new_elem[1]} from {new_elem[2]} to {(' ').join(new_elem[3:])}"
        else:
            return "Attribute does not exist"


def delete_attribute(string):
    new_elem = string.split()
    record = users.data[new_elem[0]]
    if record.delete_attribute(new_elem[1], new_elem[2]) is True:
        return f"For contact {new_elem[0]} attribute: {new_elem[1]} was deleted"
    else:
        return "Attribute does not exist"


def search(string):
    new_elem = string.split()
    return users.search_contacts(new_elem[0])


def show_all():
    if not users.data:
        return "AddressBook is empty"
    result = [record.get_info() for page in users.iterator()
              for record in page]
    return '\n'.join(result)


def delete_contact(string):
    new_elem = string.split()
    users.delete_contact(new_elem[0])
    return f"You delete contact {new_elem[0]}"


def days_to_b_day(string):
    new_elem = string.split()
    record = users[new_elem[0]]
    return f" Contact {string} has {record.day_to_b_day()} till his Birthday"


def add_address(string):
    new_elem = string.split()
    if users.data.get(new_elem[0]):
        record = users.data[new_elem[0]]
        record.add_address((" ").join(new_elem[1:]))
        return f"You added to contact {new_elem[0]} next address: {new_elem[1]}..."
    else:
        return "There is no contact with this name"


def add_notes(string):
    new_elem = string.split()
    record = users[new_elem[0]]
    to_dict = (" ").join(new_elem[1:]).split(":")
    dictionary = {to_dict[0]: to_dict[1]}
    record.add_notes(dictionary)
    return f"You add next note: '{dictionary}...' for contact: {new_elem[0]}"


def add_email(string):
    new_elem = string.split()
    record = users[new_elem[0]]
    record.add_email(new_elem[1])
    return f"You add next email: {new_elem[1]} for contact: {new_elem[0]}"


def stop():
    return "Good bye!"


def manual():
    return '''Please enter one of the commands:
    >>hello, 
    >>add_contact 'name' 'number', 
    >>add_phone 'name' 'number', 
    >>change 'name' 'attribute' 'old_value/if not defined =0' 'new_value',
    >>search 'name' or 'part of info', 
    >>delete_attribute 'name' 'attribute' 'value',
    >>delete_contact 'name', 
    >>days_to_b_day 'name',
    >>add_email 'name' 'email',
    >>add_address 'name' 'address',
    >>add_notes 'name' 'hashtag:notes', 
    >>show_all", 
    >>exit, >>good_bye, >>close
    '''


the_end = False
users = AddressBook()
commands_dict = {"hello": hello,
                 "help": manual,
                 "add_contact": add,
                 "add_phone": add_phone,
                 "change": change_attr,
                 "search": search,
                 "delete_attribute": delete_attribute,
                 "delete_contact": delete_contact,
                 "days_to_b_day": days_to_b_day,
                 "add_email": add_email,
                 "add_address": add_address,
                 "add_notes": add_notes,
                 "show_all": show_all,
                 "exit": stop}


def main():
    try:
        print(hello())
        while not the_end:
            user_input = input("Enter please: ").lower()
            if user_input in ["good_bye", "close", "exit"]:
                print(commands_dict.get("exit")())
                break
            else:
                print(parser(user_input))
    finally:
        users.save_file()


if __name__ == '__main__':
    main()
