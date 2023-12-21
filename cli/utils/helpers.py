from time import sleep
from rich.table import Table
from rich.panel import Panel
from rich.console import Console
from rich.progress import track

def progress_bar():
    for _ in track(range(100), description='[yellow]Processing your request'):
        sleep(0.002)

def rich_console_error(text, style="red"):
    console = Console()
    text = "❌ " + str(text)
    return console.print(Panel(text, expand=True), style=style)

def rich_console(text, style="green"):
    console = Console()
    console.print(text, style=style)

def hello():
    table = Table(title="Welcome to the G7 assistant bot!", style="yellow")
    table.add_column("Commands list", style="cyan", no_wrap=True)
    table.add_column("Parameters", style="magenta")
    table.add_column("Description", justify="left", style="green")

    table.add_row("hello", "-", "shows hello message")
    table.add_row("add", "<name>'", "aadds a new contact. Arguments birthday, address and email are not required")
    table.add_row("add-phone", "<name> <phone>", "adds a new phone number")
    table.add_row("add-email", "<name> <email>", "adds an email")
    table.add_row("add-address", "<name> <address>", "adds an address")
    table.add_row("add-birthday", "<name> <birthday_date>", "adds a birthday")
    table.add_row("change", "<name> <old_phone> <phone>", "changes a phone number in the contact")
    table.add_row("change-birthday", "<name> <new_birthday_date>", "change birthday, format of date <dd.mm.YYYY>")
    table.add_row("change-name", "<name> <new_name>", "change name")
    table.add_row("change-email", "<name> <mail>", "change email")
    table.add_row("phone", "<name>", "get all phone numbers in the contact")
    table.add_row("all", "-", "get all contacts")
    table.add_row("show-birthday", "<name>", "shows a birthday")
    table.add_row("birthdays", "<days_in_advance>", "shows all birthdays in the next days in advance. <days_in_advance> is not required")
    table.add_row("search", "<search_query>", "for searching information in the contact")
    table.add_row("delete <name>", "-", "delete contact from the contact")
    table.add_row("add-note", "<title>", "adds a new note")
    table.add_row("edit-note", "<id>", "edits an existing note. If you want to get ID use 'all-notes' command")
    table.add_row("delete-note", "<id>", "deletes a note")
    table.add_row("all-notes", "-", "lists all notes")
    table.add_row("-", "-", "-")
    table.add_row("-", "-", "-")
    table.add_row("-", "-", "-")
    table.add_row("-", "-", "-")
    table.add_row("-", "-", "-")
    table.add_row("change", "<name> <old_phone> <phone>", "changes a phone number in the contact")
    table.add_row("phone", "<name>", "get all phone numbers in the contact")
    table.add_row("all", "-", "get all contacts")
    table.add_row("add-birthday", "<name> <birthday_date>", "adds a birthday")
    table.add_row("show-birthday", "<name>", "shows a birthday")
    table.add_row("exit or close", "-", "closes the app")

    console = Console()
    console.print(table)

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def parse_question_input(user_input):
    args = user_input.split()
    return args

def is_match(record, query):
    for value in record.to_dict().values():
        if value is None:
            continue

        if isinstance(value, list):
            if any(query in str(item).lower() for item in value):
                return True
        elif query in str(value).lower():
            return True

    return False

