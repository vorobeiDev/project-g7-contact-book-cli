from cli.models.address_book import AddressBook
from cli.models.notebook import Notebook

from cli.services.address_book_service import add_contact, change_contact, get_phone, get_all_contacts, add_birthday, \
    show_birthday, delete_contact, change_birthday, change_email, change_name, get_birthdays, \
    add_email, add_address, add_phone
from cli.services.file_service import write_data_to_file, read_data_from_file
from cli.services.input_helper import get_help, prompt_handler
from cli.services.notebook_service import add_note, get_all_notes, edit_note, delete_note
from cli.services.search_service import search

from cli.utils.helpers import parse_input


def main():
    book = AddressBook()
    notebook = Notebook()
    book_from_file = read_data_from_file("book.pkl")
    notebook_from_file = read_data_from_file("notebook.pkl")

    if book_from_file is not None:
        book = book_from_file
    if notebook_from_file is not None:
        notebook = notebook_from_file

    print("Welcome to the assistant bot!")
    print(get_help())
    while True:
        user_input = prompt_handler("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("Hi! How can I help you?")
        elif command == "help":
            print(get_help())
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
            print(search(args, book))
        elif command == "search-note":
            print(search(args, notebook))
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
