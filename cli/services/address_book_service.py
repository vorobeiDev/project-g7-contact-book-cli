from datetime import datetime, date
from collections import defaultdict

from cli.models.address_book import AddressBook
from cli.utils.constants import WEEKDAYS, BIRTHDAYS_DATE_FORMAT
from cli.exceptions.error_handler import error_handler
from cli.exceptions.errors import ContactNotFoundError, IncorrectArgumentsQuantityError, ContactsAreEmptyError, \
    SearchParamAreIncorrectError, NoMatchesFoundError, ContactIsAlreadyExistsError, ContactNotFoundAddressBook
from cli.models.record import Record
from cli.utils.helpers import is_match, parse_question_input


@error_handler
def add_contact(args, book: AddressBook):
    if len(args) != 1:
        raise IncorrectArgumentsQuantityError("To add a new contact use 'add <name>'command.")

    name = args[0]

    contact = book.find(name=name)
    if contact is not None:
        raise ContactIsAlreadyExistsError

    contact_information = ["phone", "email", "address", "birthday"]

    new_contact = Record(name=name)

    for key in contact_information:
        user_input = input(f"Do you want to add a {key}? (n/no - for skip): ")
        args = parse_question_input(user_input)

        if args[0].lower() in ["n", "no"]:
            continue
        else:
            value = " ".join(args)
            if key == "phone":
                new_contact.add_phone(phone=value)
            elif key == "email":
                new_contact.add_email(email=value)
            elif key == "address":
                new_contact.add_address(address=value)
            elif key == "birthday":
                new_contact.add_birthday(birthday=value)

    book.add_record(record=new_contact)
    return "Contact created!"


@error_handler
def change_contact(args, book: AddressBook):
    if len(args) != 3:
        raise IncorrectArgumentsQuantityError("Use 'change <name> <old_phone> <phone>' command for changing contact.")
    name, old_phone, phone = args
    contact = book.find(name=name)
    if contact is None:
        raise ContactNotFoundError
    contact.edit_phone(old_phone=old_phone, new_phone=phone)
    return "Contact changed."


@error_handler
def change_name(args, book: AddressBook):
    if len(args) != 2:
        raise IncorrectArgumentsQuantityError("Use 'change-name <name> <new_name>' command for changing name.")
    name, new_name = args
    contact = book.find(name=name)
    if contact is None:
        raise ContactNotFoundError

    if name == new_name:
        raise IncorrectArgumentsQuantityError("The name and new name are the same. Use different new name. New name must be different.")
    contact.change_name(new_name)
    book.add_record(contact)
    book.delete(name)

    return f"Contact {name} was changed on {new_name}."


@error_handler
def change_birthday(args, book: AddressBook):
    if len(args) != 2:
        raise IncorrectArgumentsQuantityError("Use 'change-birthday <name> <new birthday date>' command for changing birthday.")
    name, birthday = args
    contact = book.find(name=name)
    if contact is None:
        raise ContactNotFoundError
    contact.change_birthday(birthday)
    return f"Birthday for {name} was changed."


@error_handler
def change_email(args, book: AddressBook):
    if len(args) != 2:
        raise IncorrectArgumentsQuantityError("Use 'change-email <name> <email>' command for changing email.")
    name, email = args
    contact = book.find(name=name)
    if contact is None:
        raise ContactNotFoundError
    contact.change_email(email)
    return f"Email for {name} was changed."


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
    notes = None

    for part in parts:
        # Split each part into key and value based on the ':'
        key_value = part.split(':')
        
        # Clean up whitespace and assign the key-value pairs accordingly
        if len(key_value) == 2:
            key = key_value[0].strip()
            val = key_value[1].strip()
            
            if key == 'Contact name':
                contact_name = val
            elif key == 'phones':
                phones = val
            elif key == 'Birthday':
                birthday = val
            elif key == 'Email':
                email = val
            elif key == 'Notes':
                notes = val

    # Print or use the extracted keys and values
    return f"[b]{contact_name}[/b]\n[white]Phones: [yellow]{phones}\n[white]Email: [yellow]{email}\n[white]Birthday: [yellow]{birthday}\n[white]Notes: [yellow]{notes}"


@error_handler
def add_phone(args, book: AddressBook):
    if len(args) != 2:
        raise IncorrectArgumentsQuantityError("To add phone number use 'add-phone <name> <phone>' command.")
    name, phone = args
    contact = book.find(name=name)
    if contact is None:
        raise ContactNotFoundError
    contact.add_phone(phone=phone)
    return "Phone number added."


@error_handler
def add_birthday(args, book: AddressBook):
    if len(args) != 2:
        raise IncorrectArgumentsQuantityError("To add a birthday use 'add-birthday <name> <birthday_date>' command in "
                                              f"format '{BIRTHDAYS_DATE_FORMAT}'.")
    name, birthday = args
    contact = book.find(name=name)
    if contact is None:
        raise ContactNotFoundError
    # TODO: Birthday already exists
    contact.add_birthday(date=birthday)
    return "Birthday added."


@error_handler
def add_address(args, book: AddressBook):
    if len(args) < 2:
        raise IncorrectArgumentsQuantityError("To add an address use 'add-address <name> <address>' command.")
    name, *address = args
    contact = book.find(name=name)
    if contact is None:
        raise ContactNotFoundError
    # TODO: Address already exists
    contact.add_address(address=" ".join(address))
    return "Address added."


@error_handler
def add_email(args, book: AddressBook):
    if len(args) != 2:
        raise IncorrectArgumentsQuantityError("To add an email use 'add-email <name> <email>' command.")
    name, email = args
    contact = book.find(name=name)
    if contact is None:
        raise ContactNotFoundError
    # TODO: Email already exists
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
def search(args, book: AddressBook):
    records = book.find_all()

    if len(records) == 0:
        raise ContactsAreEmptyError

    if len(args) != 1:
        raise SearchParamAreIncorrectError

    query = args[0].lower()
    result = {record for name, record in records if is_match(record, query)}

    if len(result) == 0:
        raise NoMatchesFoundError

    return '\n'.join(str(record) for record in result)


@error_handler
def delete_contact(args, book: AddressBook):
    name = args[0]
    # TODO: Add input with question "Do you want to delete contact? (yes/no)"
    if name in book.keys():
        book.delete(name)
        return f"Contact {name} was deleted!"
    raise ContactNotFoundAddressBook
