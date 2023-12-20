from cli.services.file_service import write_contacts_to_file, read_contacts_from_file
from cli.utils.helpers import parse_input, process_data
from cli.services.command_service import add_contact, change_contact, get_phone, get_all_contacts_object, get_content, add_birthday, \
    show_birthday, get_birthdays_per_week, search
from cli.models.address_book import AddressBook

from rich import print as rprint
from rich.progress import track
from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel


def main():
    book = AddressBook()
    book_from_file = read_contacts_from_file("book.pkl")
    if book_from_file is not None:
        book = book_from_file
    rprint("Welcome to the assistant bot!")
    rprint("""
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

        for _ in track(range(100), description='[green]Processing your request'):
            process_data()

        if command in ["close", "exit"]:
            rprint("Good bye!")
            break
        elif command == "hello":
            rprint("Hi! How can I help you?")
        elif command == "add":
            rprint(add_contact(args, book=book))
        elif command == "change":
            rprint(change_contact(args, book=book))
        elif command == "phone":
            rprint(get_phone(args, book=book))
        elif command == "all":
            console = Console()
            users = get_all_contacts_object(book)
            user_renderables = [Panel(get_content(user), expand=True) for user in users]
            console.print(Columns(user_renderables))
        elif command == "add-birthday":
            rprint(add_birthday(args, book=book))
        elif command == "show-birthday":
            rprint(show_birthday(args, book=book))
        elif command == "birthdays":
            rprint(get_birthdays_per_week(book))
        elif command == "search":
            rprint(search(args, book=book))
        else:
            rprint("Invalid command.")

        write_contacts_to_file("book.pkl", book)


if __name__ == "__main__":
    main()
