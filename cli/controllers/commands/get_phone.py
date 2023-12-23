from cli.controllers.command import Command
from cli.exceptions.error_handler import error_handler
from cli.exceptions.errors import IncorrectArgumentsQuantityError, ContactDoesNotHavePhoneNumber
from cli.utils.console import with_console


class GetPhoneCommand(Command):
    @error_handler
    @with_console
    def execute(self):
        name = " ".join(self.args)

        if len(name) == 0:
            raise IncorrectArgumentsQuantityError("To get the user's phone number please use 'phone <name>' command.")

        contact = self.find_contact_by_name(name=name)
        if len(contact.phones) == 0:
            raise ContactDoesNotHavePhoneNumber(name)

        plural_text = "phone" if len(contact.phones) == 1 else "phones"
        return f"{name}'s {plural_text}: {', '.join(p.value for p in contact.phones)}"
