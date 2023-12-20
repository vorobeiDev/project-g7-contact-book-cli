from cli.models.address_book import AddressBook
from cli.models.notebook import Notebook

from cli.services.address_book_service import add_contact, change_contact, get_phone, get_all_contacts, add_birthday, \
    show_birthday, search, delete_contact, change_birthday, change_email, change_name, get_birthdays, \
    add_email, add_address, add_phone
from cli.services.file_service import write_data_to_file, read_data_from_file
from cli.services.notebook_service import add_note, get_all_notes, edit_note, delete_note

from cli.utils.helpers import parse_input
from rich import print as rprint


def main():
    book = AddressBook()
    notebook = Notebook()
    book_from_file = read_data_from_file("book.pkl")
    notebook_from_file = read_data_from_file("notebook.pkl")

    if book_from_file is not None:
        book = book_from_file
    rprint("Welcome to the assistant bot!")
    rprint("""
        Command list:
        'hello' - shows hello message
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
    """)
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("Hi! How can I help you?")
        elif command == "add":
            print(add_contact(args, book=book))
        elif command == "add-phone":
            print(add_phone(args, book=book))
        elif command == "add-birthday":
            print(add_birthday(args, book=book))
        elif command == "add-address":
            print(add_address(args, book=book))
        elif command == "add-email":
            print(add_email(args, book=book))
        elif command == "change":
            print(change_contact(args, book=book))
        elif command == "phone":
            print(get_phone(args, book=book))
        elif command == "all":
            print(get_all_contacts(book))
        elif command == "show-birthday":
            print(show_birthday(args, book=book))
        elif command == "birthdays":
            print(get_birthdays(book=book, days_in_advance=args[0] if args else None))
        elif command == "search":
            print(search(args, book=book))
        elif command == "delete":
            print(delete_contact(args, book=book))
        elif command == "change-birthday":
            print(change_birthday(args, book=book))
        elif command == "change-email":
            print(change_email(args, book=book))
        elif command == "change-name":
            print(change_name(args, book=book))
        elif command == "add-note":
            print(add_note(args, notebook=notebook))
        elif command == "all-notes":
            print(get_all_notes(notebook=notebook))
        elif command == "edit-note":
            print(edit_note(args, notebook=notebook))
        elif command == "delete-note":
            print(delete_note(args, notebook=notebook))
        else:
            print("Invalid command.")

        write_data_to_file("book.pkl", book)
        write_data_to_file("notebook.pkl", notebook)


if __name__ == "__main__":
    main()
