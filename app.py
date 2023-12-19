from cli.services.file_service import write_contacts_to_file, read_contacts_from_file
from cli.utils.helpers import parse_input
from cli.services.commands import add_contact, change_contact, get_phone, get_all_contacts, add_birthday, show_birthday, \
    get_birthdays_per_week
from cli.models.address_book import AddressBook


def main():
    book = AddressBook()
    book_from_file = read_contacts_from_file("book.pkl")
    if book_from_file is not None:
        book = book_from_file
    print("Welcome to the assistant bot!")
    print("""
        Command list:
        'hello' - shows hello message
        'add <name> <phone>' - adds a new contact.
        'change <name> <old_phone> <phone>' - changes a phone number in the contact
        'phone <name>' - get all phone numbers in the contact
        'all' - get all contacts
        'add-birthday <name> <birthday_date>' - adds a birthday
        'show-birthday <name>' - shows a birthday
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
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "phone":
            print(get_phone(args, book))
        elif command == "all":
            print(get_all_contacts(book))
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            print(get_birthdays_per_week(book))
        else:
            print("Invalid command.")

        write_contacts_to_file("book.pkl", book)


if __name__ == "__main__":
    main()
