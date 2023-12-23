from prompt_toolkit.shortcuts import input_dialog

from cli.exceptions.error_handler import error_handler
from cli.exceptions.errors import IncorrectArgumentsQuantityError, ContactHasNotBeenChanged
from cli.controllers.command import Command
from cli.utils.console import with_console


class AddPhoneCommand(Command):
    @error_handler
    @with_console
    def execute(self):
        name = " ".join(self.args)

        if len(name) == 0:
            raise IncorrectArgumentsQuantityError("To add phone number, use 'add-phone <name>' command.")

        contact = self.find_contact_by_name(name=name)
        phone = input_dialog(
            title=f"Add a new phone number",
            text=f"Please enter a new contact phone number:"
        ).run()

        if phone is None:
            raise ContactHasNotBeenChanged(name)

        contact.add_phone(phone=phone)
        return f"A new phone number has been added to the contact named '{name}'."
