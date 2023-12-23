from prompt_toolkit.shortcuts import input_dialog

from cli.exceptions.error_handler import error_handler
from cli.exceptions.errors import IncorrectArgumentsQuantityError, ContactHasNotBeenChanged
from cli.controllers.command import Command
from cli.utils.console import with_console


class AddBirthdayCommand(Command):
    @error_handler
    @with_console
    def execute(self):
        name = " ".join(self.args)

        if len(self.args) == 0:
            raise IncorrectArgumentsQuantityError("To add a birthday, use 'add-birthday <name>' command")

        contact = self.find_contact_by_name(name=name)
        birthday_exists = f"Contact {name} has birthday {contact.birthday}\n" if contact.birthday is not None else ""
        birthday = input_dialog(
            title=f"Add a new birthday",
            text=f"{birthday_exists}Please enter a new contact birthday:"
        ).run()

        if birthday is None:
            raise ContactHasNotBeenChanged(name)

        contact.add_birthday(birthday=birthday)
        return f"A new birthday has been added to the contact named '{name}'."
