from time import sleep
from rich.table import Table
from rich.panel import Panel
from rich.console import Console
from rich.progress import track
from prompt_toolkit.completion import NestedCompleter, WordCompleter
from prompt_toolkit.shortcuts import prompt


def progress_bar():
    for _ in track(range(100), description='[yellow]Processing your request'):
        sleep(0.00001)


def rich_console_error(text, style="red"):
    console = Console()
    text = "❌  " + str(text)
    console.print(Panel(text, expand=True), style=style)


def rich_console(text, style="green"):
    console = Console()
    console.print(text, style=style)


def print_hello():
    table = Table(title="Welcome to the G7 assistant bot!", style="yellow")
    table.add_column("Commands list", style="cyan", no_wrap=True)
    table.add_column("Parameters", style="magenta")
    table.add_column("Description", justify="left", style="green")

    table.add_row("hello", "", "shows hello message")
    table.add_row("help", "", "shows command table")
    table.add_row()

    table.add_row("add", "<name>", "adds a new contact. Arguments birthday, address and email are not required")
    table.add_row("add-phone", "<name> <phone>", "adds a new phone number")
    table.add_row("add-email", "<name> <email>", "adds an email")
    table.add_row("add-address", "<name> <address>", "adds an address")
    table.add_row("add-birthday", "<name> <birthday_date>", "adds a birthday")
    table.add_row()

    table.add_row("change", "<name> <old_phone> <phone>", "changes a phone number in the contact")
    table.add_row("change-birthday", "<name> <new_birthday_date>", "change birthday, format of date <dd.mm.YYYY>")
    table.add_row("change-name", "<name> <new_name>", "change name")
    table.add_row("change-email", "<name> <new_email>", "change email")
    table.add_row()

    table.add_row("delete", "<name>", "delete contact from the contact")
    table.add_row()

    table.add_row("phone", "<name>", "get all phone numbers in the contact")
    table.add_row("all", "", "get all contacts")
    table.add_row("show-birthday", "<name>", "shows a birthday")
    table.add_row("birthdays", "<days_in_advance>", "shows all birthdays in the next days in advance. <days_in_advance> is not required")
    table.add_row()

    table.add_row("search", "<search_query>", "for searching information in the contact")
    table.add_row("search-note", "<search_query>", "for searching information in the notes")
    table.add_row()

    table.add_row("add-note", "<title>", "adds a new note")
    table.add_row("edit-note", "<id>", "edits an existing note. If you want to get ID use 'all-notes' command")
    table.add_row("delete-note", "<id>", "deletes a note")
    table.add_row("all-notes", "", "lists all notes")
    table.add_row()

    table.add_row("exit or close", "", "closes the app")

    console = Console()
    console.print(table)


completer = NestedCompleter.from_nested_dict({
    "hello": None,
    "help": None,
    "exit": None,
    "close": None,
    "add": {"<name>"},
    "add-phone": {"<name> <phone>"},
    "add-email": {"<name> <email>"},
    "add-address": {"<name> <address>"},
    "add-birthday": {"<name> <birthday>"},
    "change": {"<name> <old_phone> <new_phone>"},
    "change-birthday": {"<name> <new_birthday_date>"},
    "change-name": {"<name> <new_name>"},
    "change-email": {"<name> <new_email>"},
    "change-address": {"<name> <new_address>"},
    "phone": {"<name>"},
    "all": None,
    "show-birthday": {"<name>"},
    "birthdays": {"<days_in_advance>"},
    "search": {"<search_query>"},
    "delete": {"<name>"},
    "add-note": {"<title>"},
    "edit-note": {"<id>"},
    "delete-note": {"<id>"},
    "all-notes": None,
})

answer_completer = WordCompleter(["no", "n"])


def answer_prompt_handler(message:str):
    return prompt(
        message=message,
        completer=answer_completer
    )


def prompt_handler(message: str):
    return prompt(
        message=message,
        completer=completer)
