from cli.models.address_book import AddressBook
from cli.models.note import Note
from cli.models.notebook import Notebook
from cli.services.command_service import command_service

from cli.services.file_service import write_data_to_file, read_data_from_file
from cli.services.input_helper import prompt_handler, print_hello, \
    progress_bar, rich_console, rich_console_error

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
        Note.counter = len(notebook) + 1

    print_hello()

    entry = {
        "book": book,
        "notebook": notebook
    }

    while True:
        user_input = prompt_handler("Enter a command: ")
        command, *args = parse_input(user_input)

        progress_bar()

        if command in ["close", "exit"]:
            rich_console("Good bye!")
            break

        if command == "hello":
            rich_console("Hi! How can I help you?")
        elif command == "help":
            print_hello()
        elif command_service.has_command(command):
            command_service.run(command, args, entry)

        else:
            rich_console_error("Invalid command.")

        write_data_to_file("book.pkl", book)
        write_data_to_file("notebook.pkl", notebook)


if __name__ == "__main__":
    main()
