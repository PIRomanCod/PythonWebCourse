# Python_Core_Team5_project

"Personal assistant", application features:

1. saves contacts with names, addresses, phone numbers, email and birthdays to the contact book;
2. display a list of contacts whose birthday is a given number of days from the current date;
3. checks the correctness of the entered phone number and email when creating or editing a record and notifies the user in case of incorrect entry;
4. searches for contacts among contacts in the book;
5. edits and deletes records from the contact book;
6. saves notes with text information;
7. searches for notes;
8. edits and deletes notes;
9. adds "tags" to the notes, keywords describing the subject and subject of the record;
10. searches and sorts notes by keywords (tags);
11. sorts files in the specified folder by categories (images, documents, videos, etc.).
12. analyzes the entered text and tries to guess what the user wants from it and suggests the closest command to execute
13. save information on the hard drive in binary format and can be restarted without lost data

# Install "Personal assistant"

For installation in your system:

1.  Use venv for creating virtual environment:

    1.1. for creating new virtual environment run in console the command:

        - python3 -m venv /path/to/new/virtual/environment
          or
        - venv /path/to/new/virtual/environment

    1.2. for activating new virtual environment run in console the command:

        - \path\to\new\virtual\environment\Scripts\activate.bat (Windows)
        - source /path/to/new/virtual/environment/bin/activate (Linux / Mac OS)
        - \path\to\new\virtual\environment\Scripts\Activate.ps1 (if you use PowerShell console)

    1.3. for deactivating new virtual environment run in console the command:

        - deactivate

    1.4. for full deleting new virtual environment just delete all folder: \path\to\new\virtual\environment\

2.  For installing the "Personal assistant" after activating new virtual environment run in console the command:

    -   pip install -e
    -   after installation, package assistant_bot appears in the system

3.  For start application run in console the command:
    -   pa

# Users Manual

During the launch process, the program loads the previously created address book (if it exists)

The program has the function of predictive dialing, which makes it easier to work with it. In the process of typing, available commands appear in the address bar, which can be selected with the tab + space button. Also, the predictive dialing covers already existing contacts.

Commands list: 

    >>help - shows next commands list

    >>add_contact 'name' 'number (3 operator and 7 numbers digit)'
       - to create a new contact in your contact book-  run the command with 2 arguments with space separating: 'Name of contact' 'Phone number'

    >>add_phone 'name' 'number (3 operator and 7 numbers digit)'
       - to add an additional phone number to an existing contact -  run the command with 2 arguments with space separating: 'Name of contact' 'Phone number'

    >>add_note: 'name'(or 'unnamed') 'the note text' '#hashtag' '#hashtag'...
        - to add notes to an existing contact - run the command with at least 2 arguments with space separating, hashtags unnecessary: 'Name of contact' 'note text' '#hashtag' '#hashtag'...

    >>edit 'attribute (one of: phones, notes, birthday, email, address)'
                  'name' 'phone'  'new_value',
                  'note' 'start with.. - change if only one match found'
                        '->' 'new text' (hashtag stay the same)
                  'birthday' 'new_value',
                  'email' 'new_value',
                  'address' 'new_value'

    >>search 'name' or 'part of info'
        - to search in your contact book - run the command with 1 argument: full or partial of any information

    >>delete_info 'name' 'attribute (one of: phones, notes, birthday, email, address)' 'value'
                         'name' 'phone' 'value',
                         'note' 'start with..' - delete if only one match found
                         'notes' 'all'  - delete all notes
                         'birthday'
                         'email'
                         'address'

    >>delete_contact 'name'
        - to remove a contact from the contact book - run the command with 1 argument: 'Name of contact'

    >>days_to_birthday 'name'
        - to understand how many days are left until the contact's birthday  - run the command with 1 argument: 'Name of contact' (of course if you fill the information before)

    >>birthday_list 'period days'
        - to understand which contacts in your contact book have the birthdays in some period  - run the command with 1 argument: 'amount of days'

    >>find_tag 'tag'
        - to search some 'tag' in your contact book notes - run the command with 1 argument: full or partial of information

    >>find_text 'text'
        - to search some 'text' in your contact book notes - run the command with 1 argument: full or partial of information

    >>show_all
        - to show all existing information in your contact book

    >>sort
        - to sort files in the specified folder by categories (images, documents, videos, etc.) - run the command with 1 argument: 'absolut path to specified folder'

    >>exit, >>good_bye, >>close
        - to save and closed the application

Thank you for choosing our product
