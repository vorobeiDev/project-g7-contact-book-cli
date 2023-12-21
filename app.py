from cli.services.file_service import write_contacts_to_file, read_contacts_from_file
from cli.utils.helpers import parse_input, process_data, hello, rich_console, rich_console_error, progress_bar
from cli.services.command_service import add_contact, change_contact, get_phone, get_all_contacts_object, get_content, add_birthday, \
    show_birthday, get_birthdays_per_week, search
from cli.models.address_book import AddressBook

from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel



def main():
    book = AddressBook()
    console = Console()
    book_from_file = read_contacts_from_file("book.pkl")
    
    if book_from_file is not None:
        book = book_from_file
    
    hello()

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        progress_bar()

        if command in ["close", "exit"]:
            rich_console("Good bye!")
            break
        elif command == "hello":
            rich_console("Hi! How can I help you?")
        elif command == "add":
            rich_console(add_contact(args, book=book))
        elif command == "change":
            rich_console(change_contact(args, book=book))
        elif command == "phone":
            rich_console(get_phone(args, book=book))
        elif command == "all":
            users = get_all_contacts_object(book)
            user_renderables = [Panel(get_content(user), expand=True) for user in users]
            console.print(Columns(user_renderables))
        elif command == "add-birthday":
            rich_console(add_birthday(args, book=book))
        elif command == "show-birthday":
            rich_console(show_birthday(args, book=book))
        elif command == "birthdays":
            rich_console(get_birthdays_per_week(book))
        elif command == "search":
            rich_console(search(args, book=book))
        else:
            rich_console_error("Invalid command.")

        write_contacts_to_file("book.pkl", book)


if __name__ == "__main__":
    main()
