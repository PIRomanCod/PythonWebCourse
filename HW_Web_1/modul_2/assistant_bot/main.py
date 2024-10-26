''' 
1. Нарисуйте UML диаграмму вашего выпускного проекта "Персональный помощник" с прошлого курса

2. Модифицируйте код вашего приложения, чтобы представление информации пользователю 
(вывод карточек с контактами пользователя, заметками, страничка с информацией о доступных командах)
было легко изменить. Для этого надо описать абстрактный базовый класс для пользовательских представлений и конкретные реализации,
которые наследуют базовый класс и реализуют консольный интерфейс.
'''

from functions import commands_dict, parser, users, hello
import addressbook
import console


the_end = False


def main():
    try:
        print(hello())
        while not the_end:
            user_input = console.get_input("Enter please: ").lower()
            if user_input in ["good_bye", "close", "exit"]:
                print(commands_dict.get("exit")())
                break
            else:
                print(parser(user_input))
    finally:
        users.save_file()


if __name__ == '__main__':
    main()
