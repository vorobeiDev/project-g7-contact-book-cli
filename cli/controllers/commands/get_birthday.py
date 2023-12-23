from prompt_toolkit.shortcuts import input_dialog

from cli.exceptions.error_handler import error_handler
from cli.exceptions.errors import IncorrectArgumentsQuantityError, ContactHasNotBeenChanged, \
    ContactDoesNotHaveDateOfBirth
from cli.controllers.command import Command
from cli.utils.console import with_console


class GetBirthdayCommand(Command):
    @error_handler
    @with_console
    def execute(self):
        name = " ".join(self.args)

        if len(self.args) == 0:
            raise IncorrectArgumentsQuantityError("To show a birthday, use 'birthday <name>' command.")

        contact = self.find_contact_by_name(name=name)

        if contact.birthday is None:
            raise ContactDoesNotHaveDateOfBirth(name)

        return f"Date of birth for the contact '{name}' is {contact.birthday}"
