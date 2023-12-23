from cli.controllers.commands.add_address import AddAddressCommand
from cli.controllers.commands.add_birthday import AddBirthdayCommand
from cli.controllers.commands.add_contact import AddContactCommand
from cli.controllers.commands.add_email import AddAEmailCommand
from cli.controllers.commands.add_note import AddNoteCommand
from cli.controllers.commands.add_phone import AddPhoneCommand
from cli.controllers.commands.add_tag import AddTagCommand
from cli.controllers.commands.change_contact import ChangeContactCommand
from cli.controllers.commands.change_note import ChangeNoteCommand
from cli.controllers.commands.delete_contact import DeleteContactCommand
from cli.controllers.commands.delete_note import DeleteNoteCommand
from cli.controllers.commands.delete_tag import DeleteTagCommand
from cli.controllers.commands.get_all import GetAllCommand
from cli.controllers.commands.get_birthday import GetBirthdayCommand
from cli.controllers.commands.get_birthdays import GetBirthdaysCommand
from cli.controllers.commands.get_phone import GetPhoneCommand
from cli.controllers.commands.search import SearchCommand


commands = {
    "add": AddContactCommand,
    "add-phone": AddPhoneCommand,
    "add-birthday": AddBirthdayCommand,
    "add-address": AddAddressCommand,
    "add-email": AddAEmailCommand,
    "change": ChangeContactCommand,
    "delete": DeleteContactCommand,

    "birthdays": GetBirthdaysCommand,
    "birthday": GetBirthdayCommand,
    "phone": GetPhoneCommand,

    "search": SearchCommand,
    "search-note": SearchCommand,

    "all": GetAllCommand,
    "all-notes": GetAllCommand,

    "add-note": AddNoteCommand,
    "change-note": ChangeNoteCommand,
    "delete-note": DeleteNoteCommand,
    "add-tag": AddTagCommand,
    "delete-tag": DeleteTagCommand,
}

contact_commands = [
    "add", "add-phone", "add-birthday", "add-address",
    "add-email", "change", "delete", "birthdays",
    "birthday", "phone", "search", "all"
]


class CommandService:
    @staticmethod
    def has_command(command):
        return command in commands

    @staticmethod
    def run(command, args, entry):
        entry = entry["book"] if command in contact_commands else entry["notebook"]
        command_obj = commands[command](args, entry)
        command_obj.execute()


command_service = CommandService()
