from prompt_toolkit.shortcuts import input_dialog

from cli.exceptions.error_handler import error_handler
from cli.exceptions.errors import IncorrectArgumentsQuantityError, ContactIsNotCreatedError, ContactIsAlreadyExistsError
from cli.controllers.command import Command
from cli.models.record import Record
from cli.utils.console import with_console


class AddContactCommand(Command):
    @error_handler
    @with_console
    def execute(self):
        if len(self.args) != 0:
            raise IncorrectArgumentsQuantityError("To add a new contact, use 'add' command.")

        name = input_dialog(
            title="Create a new Contact",
            text="Please enter a name for a new contact:"
        ).run()

        if name is None:
            raise ContactIsNotCreatedError

        contact = self.entry.find(name=name)

        if contact is not None:
            raise ContactIsAlreadyExistsError

        contact_information = ["phone", "email", "address", "birthday"]

        new_contact = Record(name=name)

        for key in contact_information:
            value = input_dialog(
                title=f"Add a {key}",
                text=f"Please enter a contact {key}:",
                ok_text="Add",
                cancel_text="Skip"
            ).run()

            if value is None:
                continue
            else:
                if key == "phone":
                    new_contact.add_phone(phone=value)
                elif key == "email":
                    new_contact.add_email(email=value)
                elif key == "address":
                    new_contact.add_address(address=value)
                elif key == "birthday":
                    new_contact.add_birthday(birthday=value)

        self.entry.add_record(record=new_contact)
        return f"Contact with name '{name}' has been created!"
