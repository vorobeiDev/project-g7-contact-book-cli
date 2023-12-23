from time import sleep

from rich.columns import Columns
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


def rich_console_warning(text, style="yellow"):
    console = Console()
    text = "🚨   " + str(text)
    console.print(Panel(text, expand=True), style=style)


def rich_console_table(text):
    console = Console()
    console.print(Columns(text, equal=True))


def rich_console(text, style="green"):
    console = Console()
    text = "✅   " + str(text)
    console.print(Panel(text, expand=True), style=style)


def print_hello():
    table = Table(title="Welcome to the G7 assistant bot!", style="yellow")
    table.add_column("Commands list", style="cyan", no_wrap=True)
    table.add_column("Parameters", style="magenta")
    table.add_column("Description", justify="left", style="green")

    table.add_row("hello", "", "show hello message")
    table.add_row("help", "", "show command table")
    table.add_row()

    table.add_row("add", "", "add a new contact.")
    table.add_row("add-phone", "<name>", "add a new phone number")
    table.add_row("add-email", "<name>", "add an email")
    table.add_row("add-address", "<name>", "add an address")
    table.add_row("add-birthday", "<name>", "add a birthday")
    table.add_row()

    table.add_row("change", "<name>", "change the contact information")
    table.add_row()

    table.add_row("delete", "<name>", "delete contact from the contact")
    table.add_row()

    table.add_row("all", "", "get all contacts")
    table.add_row("phone", "<name>", "get all phone numbers in the contact")
    table.add_row("birthday", "<name>", "show a birthday")
    table.add_row("birthdays", "<days_in_advance>", "show all birthdays in "
                                                    "the next days in advance. <days_in_advance> is not required")
    table.add_row()

    table.add_row("search", "<search_query>", "for searching information in the contact")
    table.add_row("search-note", "<search_query>", "for searching information in the notes")
    table.add_row()

    table.add_row("add-note", "", "add a new note")
    table.add_row("change-note", "<id>", "edit an existing note."
                                         " If you want to get ID use 'all-notes' command")
    table.add_row("delete-note", "<id>", "delete a note")
    table.add_row("all-notes", "", "list all notes")
    table.add_row()

    table.add_row("add-tag", "<note_id>", "add a new tag to the existing note with <note_id>")
    table.add_row("delete-tag", "<note_id>", "delete a tag from the existing note with <note_id>")

    table.add_row("exit or close", "", "closes the app")

    console = Console()
    console.print(table)


completer = NestedCompleter.from_nested_dict({
    "hello": None,
    "help": None,
    "exit": None,
    "close": None,
    "add": None,
    "add-phone": {"<name>"},
    "add-email": {"<name>"},
    "add-address": {"<name>"},
    "add-birthday": {"<name>"},
    "change": {"<name>"},
    "phone": {"<name>"},
    "all": None,
    "birthday": {"<name>"},
    "birthdays": {"<days_in_advance>"},
    "search": {"<search_query>"},
    "search-note": {"<search_query>"},
    "delete": {"<name>"},
    "add-note": None,
    "change-note": {"<id>"},
    "delete-note": {"<id>"},
    "add-tag": {"<id>"},
    "delete-tag": {"<id>"},
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
