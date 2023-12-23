from prompt_toolkit.shortcuts import input_dialog

from cli.controllers.command import Command
from cli.exceptions.error_handler import error_handler
from cli.exceptions.errors import IncorrectArgumentsQuantityError, ContactHasNotBeenChanged
from cli.utils.console import with_console


class AddAEmailCommand(Command):
    @error_handler
    @with_console
    def execute(self):
        name = " ".join(self.args)

        if len(self.args) == 0:
            raise IncorrectArgumentsQuantityError("To add an email, use 'add-email <name>' command.")

        contact = self.find_contact_by_name(name=name)
        email_exists = f"Contact {name} has email {contact.email}\n" if contact.email is not None else ""
        email = input_dialog(
            title=f"Add a new email",
            text=f"{email_exists}Please enter a new contact email:"
        ).run()

        if email is None:
            raise ContactHasNotBeenChanged(name)

        contact.add_email(email=email)
        return f"A new email has been added to the contact named '{name}'."
