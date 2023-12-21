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
from rich.table import Table


def main():
    book = AddressBook()
    book_from_file = read_contacts_from_file("book.pkl")
    if book_from_file is not None:
        book = book_from_file
    
    table = Table(title="Welcome to the assistant bot!")
    table.add_column("Command list", style="cyan", no_wrap=True)
    table.add_column("Parameters", style="magenta")
    table.add_column("Description", justify="left", style="green")

    table.add_row("hello", "-", "shows hello message")
    table.add_row("add", "<name> <phone>", "adds a new contact")
    table.add_row("change", "<name> <old_phone> <phone>", "changes a phone number in the contact")
    table.add_row("phone", "<name>", "get all phone numbers in the contact")
    table.add_row("all", "-", "get all contacts")
    table.add_row("add-birthday", "<name> <birthday_date>", "adds a birthday")
    table.add_row("show-birthday", "<name>", "shows a birthday")
    table.add_row("exit or close", "-", "closes the app")
    console = Console()
    console.print(table)

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
