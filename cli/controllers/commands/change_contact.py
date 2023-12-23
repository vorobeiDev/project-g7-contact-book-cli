from prompt_toolkit.shortcuts import radiolist_dialog, input_dialog

from cli.controllers.command import Command
from cli.exceptions.error_handler import error_handler
from cli.exceptions.errors import IncorrectArgumentsQuantityError, ContactHasNotBeenChanged
from cli.models.record import Record
from cli.utils.console import with_console


class ChangeContactCommand(Command):
    @error_handler
    @with_console
    def execute(self):
        name = " ".join(self.args)

        if len(name) == 0:
            raise IncorrectArgumentsQuantityError("Use 'change <name>' command for changing contact information.")

        contact = self.find_contact_by_name(name=name)

        key = radiolist_dialog(
            title="Change contact",
            text="Which param do you want to change?",
            values=[
                ("name", "Contact name"),
                ("phone", "Contact phone number"),
                ("email", "Contact email"),
                ("address", "Contact address"),
                ("birthday", "Contact birthday")
            ]
        ).run()

        if key is None:
            raise ContactHasNotBeenChanged(name)

        if key == "name":
            new_name = self.get_new_value(key, name)
            self.entry.delete(name=name)
            self.entry.add_record(self.copy_contact_with_new_name(new_name=new_name, contact=contact))
        elif key == "email":
            value = self.get_new_value(key, name)
            contact.change_email(new_email=value)
        elif key == "address":
            value = self.get_new_value(key, name)
            contact.change_address(new_address=value)
        elif key == "birthday":
            value = self.get_new_value(key, name)
            contact.change_birthday(new_birthday=value)
        elif key == "phone":
            if len(contact.phones) == 0:
                value = self.get_new_value("phone number", name)
                contact.add_phone(value)
            else:
                old_phone = self.get_old_phone(contact.phones, name)
                value = self.get_new_value("phone number", name)
                contact.change_phone(old_phone=old_phone, new_phone=value)

        return f"Contact '{contact.name}' has been changed."

    @staticmethod
    def get_new_value(key, name):
        value = input_dialog(
            title=f"Change contact {key}",
            text=f"Please enter a new contact {key}:"
        ).run()

        if value is None:
            raise ContactHasNotBeenChanged(name)

        return value

    @staticmethod
    def get_old_phone(phones, name):
        values = [(str(phone), str(phone)) for phone in phones]
        old_phone = radiolist_dialog(
            title="Change contact",
            text="Which phone's number do you want to change?",
            values=values
        ).run()

        if old_phone is None:
            raise ContactHasNotBeenChanged(name)

        return old_phone

    @staticmethod
    def copy_contact_with_new_name(new_name, contact):
        new_contact = Record(name=new_name)
        new_contact.phones = contact.phones if len(contact.phones) else []
        new_contact.email = contact.email if contact.email else None
        new_contact.birthday = contact.birthday if contact.birthday else None
        new_contact.address = contact.address if contact.address else None
        return new_contact
