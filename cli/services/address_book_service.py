from prompt_toolkit.shortcuts import yes_no_dialog, input_dialog, radiolist_dialog

from datetime import datetime, date
from collections import defaultdict

from cli.models.address_book import AddressBook
from cli.utils.constants import WEEKDAYS, BIRTHDAYS_DATE_FORMAT
from cli.exceptions.error_handler import error_handler
from cli.exceptions.errors import ContactNotFoundError, IncorrectArgumentsQuantityError, ContactsAreEmptyError, \
    ContactIsAlreadyExistsError, ContactNotFoundAddressBook, ContactHasNotBeenChanged
from cli.models.record import Record


@error_handler
def add_contact(args, book: AddressBook):
    if len(args) != 0:
        raise IncorrectArgumentsQuantityError("To add a new contact use 'add' command.")

    name = input_dialog(
        title="Create new contact",
        text="Please enter a name for a new contact:"
    ).run()

    if name is None:
        return "Contact isn't created!"

    contact = book.find(name=name)
    if contact is not None:
        raise ContactIsAlreadyExistsError

    contact_information = ["phone", "email", "address", "birthday"]

    new_contact = Record(name=name)

    for key in contact_information:
        value = input_dialog(
            title=f"Add a {key}",
            text=f"Please enter a contact {key}:"
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

    book.add_record(record=new_contact)
    return "Contact is created!"


def get_new_value(key):
    value = input_dialog(
        title=f"Change contact {key}",
        text=f"Please enter a new contact {key}:"
    ).run()
    if value is None:
        raise ContactHasNotBeenChanged
    return value


def get_old_phone(phones):
    values = [(str(phone), str(phone)) for phone in phones]
    old_phone = radiolist_dialog(
        title="Change contact",
        text="Which phone's number do you want to change?",
        values=values
    ).run()
    if old_phone is None:
        raise ContactHasNotBeenChanged
    return old_phone


def copy_contact_with_new_name(new_name, contact):
    new_contact = Record(name=new_name)
    new_contact.phones = contact.phones if len(contact.phones) else []
    new_contact.email = contact.email if contact.email else None
    new_contact.birthday = contact.birthday if contact.birthday else None
    new_contact.address = contact.address if contact.address else None
    return new_contact


@error_handler
def change_contact(args, book: AddressBook):
    name = " ".join(args)

    if len(name) == 0:
        raise IncorrectArgumentsQuantityError("Use 'change <name>' command for changing contact information.")

    contact = book.find(name=name)

    if contact is None:
        raise ContactNotFoundError

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
        new_name = get_new_value(key)
        book.delete(name=name)
        book.add_record(copy_contact_with_new_name(new_name=new_name, contact=contact))
    elif key == "email":
        value = get_new_value(key)
        contact.change_email(new_email=value)
    elif key == "address":
        value = get_new_value(key)
        contact.change_address(new_address=value)
    elif key == "birthday":
        value = get_new_value(key)
        contact.change_birthday(new_birthday=value)
    elif key == "phone":
        if len(contact.phones) == 0:
            value = get_new_value("phone number")
            contact.add_phone(value)
        else:
            old_phone = get_old_phone(contact.phones)
            value = get_new_value("phone number")
            contact.change_phone(old_phone=old_phone, new_phone=value)

    return f"Contact {contact.name} is changed."


@error_handler
def get_phone(args, book: AddressBook):
    if len(args) != 1:
        raise IncorrectArgumentsQuantityError("To get the user's phone number please use 'phone <name>' command.")
    name = args[0]
    contact = book.find(name=name)
    if contact is None:
        raise ContactNotFoundError
    phones = contact.phones
    plural_text = "phone" if len(phones) == 1 else "phones"
    return f"{name}'s {plural_text}: {', '.join(p.value for p in phones)}"


@error_handler
def get_all_contacts_object(book: AddressBook):
    records = book.find_all()
    return records


@error_handler
def get_all_contacts(book: AddressBook):
    records = book.find_all()
    if len(records) == 0:
        raise ContactsAreEmptyError
    return "\n".join([str(record) for _, record in records])


@error_handler
def get_contacts_content(contact):
    """Extract text from user dict."""
    key, value = contact  # Unpack the tuple into key and value variables
    value = str(value)
    # Split the value string based on the delimiter ';'
    parts = value.split(';')
    
    # Initialize variables to store extracted keys and values
    contact_name = None
    phones = None
    birthday = None
    email = None
    address = None

    for part in parts:
        # Split each part into key and value based on the ':'
        key_value = part.split(':')
        
        # Clean up whitespace and assign the key-value pairs accordingly
        if len(key_value) == 2:
            key = key_value[0].strip()
            val = key_value[1].strip()

            if key == 'Contact name':
                contact_name = val
            elif key == 'Phones':
                phones = val
            elif key == 'Birthday':
                birthday = val
            elif key == 'Email':
                email = val
            elif key == 'Address':
                address = val

    # Print or use the extracted keys and values
    return f"[b]{contact_name}[/b]\n[white]Phones: [yellow]{phones}\n[white]Email: [yellow]{email}\n[white]Birthday: [yellow]{birthday}\n[white]Address: [yellow]{address}"


@error_handler
def add_phone(args, book: AddressBook):
    name = " ".join(args)
    if len(name) == 0:
        raise IncorrectArgumentsQuantityError("To add phone number use 'add-phone <name>' command.")
    contact = book.find(name=name)
    if contact is None:
        raise ContactNotFoundError
    phone = input_dialog(
        title=f"Add a new phone number",
        text=f"Please enter a new contact phone number:"
    ).run()
    if phone is None:
        raise ContactHasNotBeenChanged(name)

    contact.add_phone(phone=phone)
    return "Phone number added."


@error_handler
def add_birthday(args, book: AddressBook):
    name = " ".join(args)
    if len(args) == 0:
        raise IncorrectArgumentsQuantityError("To add a birthday use 'add-birthday <name>' command")
    contact = book.find(name=name)
    if contact is None:
        raise ContactNotFoundError

    birthday_exists = f"Contact {name} has birthday {contact.birthday}\n" if contact.birthday is not None else ""

    birthday = input_dialog(
        title=f"Add a new birthday",
        text=f"{birthday_exists}Please enter a new contact birthday:"
    ).run()
    if birthday is None:
        raise ContactHasNotBeenChanged(name)
    contact.add_birthday(birthday=birthday)
    return "Birthday added."


@error_handler
def add_address(args, book: AddressBook):
    name = " ".join(args)
    if len(args) == 0:
        raise IncorrectArgumentsQuantityError("To add an address use 'add-address <name>' command")
    contact = book.find(name=name)
    if contact is None:
        raise ContactNotFoundError

    address_exists = f"Contact {name} has address {contact.address}\n" if contact.address is not None else ""

    address = input_dialog(
        title=f"Add a new address",
        text=f"{address_exists}Please enter a new contact address:"
    ).run()
    if address is None:
        raise ContactHasNotBeenChanged(name)
    contact.add_address(address=address)
    return "Address added."


@error_handler
def add_email(args, book: AddressBook):
    name = " ".join(args)
    if len(args) == 0:
        raise IncorrectArgumentsQuantityError("To add an email use 'add-email <name>' command.")
    contact = book.find(name=name)
    if contact is None:
        raise ContactNotFoundError

    email_exists = f"Contact {name} has email {contact.email}\n" if contact.email is not None else ""

    email = input_dialog(
        title=f"Add a new email",
        text=f"{email_exists}Please enter a new contact email:"
    ).run()
    if email is None:
        raise ContactHasNotBeenChanged(name)
    contact.add_email(email=email)
    return "Email added."


@error_handler
def show_birthday(args, book: AddressBook):
    if len(args) != 1:
        raise IncorrectArgumentsQuantityError("To show a birthday use 'show-birthday <name> command'.")
    name = args[0]
    contact = book.find(name=name)
    if contact is None:
        raise ContactNotFoundError
    # TODO: Don't show if a user doesn't have a birthday
    return f"{name} was born in {contact.birthday}"


@error_handler
def get_birthdays(book: AddressBook, days_in_advance = None):
    if days_in_advance is None:
        print("You can add days in advance. Use command 'birthdays <days_in_advance>. Default days in advance is 7")
    days_in_advance = int(days_in_advance) if days_in_advance is not None else 7
    today = date.today()
    birthdays = defaultdict(list)
    records = book.find_all()

    for name, user in records:
        if user.birthday is not None:
            birthday_str = str(user.birthday)
            birthday = datetime.strptime(birthday_str, BIRTHDAYS_DATE_FORMAT).date()
            birthday_this_year = birthday.replace(year=today.year)

            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)

            delta_days = (birthday_this_year - today).days

            if delta_days < days_in_advance:
                weekday = birthday_this_year.weekday()
                if weekday in [5, 6]:
                    weekday = 0

                weekday_name = WEEKDAYS[weekday]
                birthdays[weekday_name].append(name)

    plural = "" if days_in_advance == 1 else "s"
    if len(birthdays) == 0:
        return f"No birthdays in next {days_in_advance} day{plural}."

    for day in WEEKDAYS:
        if birthdays[day]:
            return f"{day}: {', '.join((birthdays[day]))}"


@error_handler
def delete_contact(args, book: AddressBook):
    name = args[0]

    result = yes_no_dialog(
        title="Delete contact",
        text="Do you want to delete contact?").run()

    if result:
        if name in book.keys():
            book.delete(name)
            return f"Contact {name} was deleted!"
        raise ContactNotFoundAddressBook
    else:
        return f"Contact {name} doesn't deleted!"
