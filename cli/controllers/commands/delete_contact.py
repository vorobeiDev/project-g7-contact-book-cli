from prompt_toolkit.shortcuts import yes_no_dialog

from cli.controllers.command import Command
from cli.exceptions.error_handler import error_handler
from cli.exceptions.errors import ContactHasNotBeenDeleted, IncorrectArgumentsQuantityError
from cli.utils.console import with_console


class DeleteContactCommand(Command):
    @error_handler
    @with_console
    def execute(self):
        name = " ".join(self.args)

        if len(name) == 0:
            raise IncorrectArgumentsQuantityError("To delete a contact, use the 'delete <name>' command.")

        contact = self.find_contact_by_name(name=name)

        result = yes_no_dialog(
            title=f"Delete contact {contact.name}",
            text=f"Do you want to delete contact with name '{name}'?",
            yes_text="Yes, delete!"
        ).run()

        if result is False:
            raise ContactHasNotBeenDeleted(name)

        self.entry.delete(name)
        return f"Contact named '{name}' has been deleted!"
