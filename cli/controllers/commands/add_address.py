from prompt_toolkit.shortcuts import input_dialog

from cli.controllers.command import Command
from cli.exceptions.error_handler import error_handler
from cli.exceptions.errors import IncorrectArgumentsQuantityError, ContactHasNotBeenChanged
from cli.utils.console import with_console


class AddAddressCommand(Command):
    @error_handler
    @with_console
    def execute(self):
        name = " ".join(self.args)

        if len(self.args) == 0:
            raise IncorrectArgumentsQuantityError("To add an address, use 'add-address <name>' command")

        contact = self.find_contact_by_name(name=name)
        address_exists = f"Contact {name} has address {contact.address}\n" if contact.address is not None else ""
        address = input_dialog(
            title=f"Add a new address",
            text=f"{address_exists}Please enter a new contact address:"
        ).run()

        if address is None:
            raise ContactHasNotBeenChanged(name)

        contact.add_address(address=address)
        return f"A new address has been added to the contact named '{name}'."
