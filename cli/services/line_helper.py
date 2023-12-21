def help():
    return """
        Command list:
        'hello' - shows hello message
        'help' - shows this
        ---
        'add <name>' - adds a new contact. Arguments birthday, address and email are not required.
        'add-phone <name> <phone>' - adds a new phone number
        'add-email <name> <email>' - adds an email
        'add-address <name> <address>' - adds an address
        'add-birthday <name> <birthday_date>' - adds a birthday
        ---
        'change <name> <old_phone> <phone>' - changes a phone number in the contact
        'change-birthday <name> <new_birthday_date>' - change birthday, format of date <dd.mm.YYYY>
        'change-name <name> <new_name>' - change name
        'change-email <name> <mail>' - change email
        ---
        'phone <name>' - get all phone numbers in the contact
        'all' - get all contacts
        'show-birthday <name>' - shows a birthday
        'birthdays <days_in_advance>' - shows all birthdays in the next days in advance. <days_in_advance> is not required.
        ---
        'search <search_query>' - for searching information in the contact
        'delete <name>' - delete contact from the contact
        ---
        'add-note <title>' - adds a new note.
        'edit-note <id>' - edits an existing note. If you want to get ID use 'all-notes' command.
        'delete-note <id>' - deletes a note.
        'all-notes' - lists all notes.
        ---
        'exit' or 'close' - closes the app
    """
