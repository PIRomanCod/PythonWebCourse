from functions import users
from prompt_toolkit import prompt
from prompt_toolkit.completion import NestedCompleter


# взял команды из текущего хелпа. нужно будет тут модифицировать при изменениях
def get_input(prompt_text: str):
    name_dict = dict()
    name_dict_ext = dict()
    for name in users:
        name_dict.update({name: None})
        name_dict_ext.update({name: {
            'phones': {str(phone): None for phone in users[name].phones},
            'note': None,
            'notes': {'all': None},
            'birthday': None,
            'email': {str(users[name].email) if users[name].email else '0': None},
            'address': None}})

    completer = NestedCompleter.from_nested_dict({
        'help': None,
        'add_contact': None,
        'add_phone': name_dict,
        'add_note': name_dict,
        'edit': name_dict_ext,
        'search_info': name_dict,
        'delete_info': name_dict_ext,
        'delete_contact': name_dict,
        'days_to_birthday': name_dict,
        'find_tag': None,
        'find_text': None,
        'birthday_list': None,
        'show_all': None,
        'sort': None,
        'exit': None,
        'good_bye': None,
        'close': None,
    })

    return prompt(prompt_text, completer=completer)
