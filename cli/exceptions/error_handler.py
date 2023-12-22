from .errors import ContactExistsError, ContactNotFoundError, \
    ContactIsAlreadyExistsError, ContactNotFoundAddressBook, NoteNotFoundError, \
    NoteAlreadyExistsError, NotesListIsEmptyError, \
    IncorrectArgumentsQuantityError, ContactsAreEmptyError, PhoneValidationError, BirthdayValidationError, \
    SearchParamAreIncorrectError, NoMatchesFoundError
from cli.utils.helpers import rich_console_error


def error_handler(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ContactExistsError as e:
            error_message = "Contact already exists."
            error = f"{error_message} {str(e)}" if e else error_message
            rich_console_error(error)
            return "\n"
        except ContactNotFoundError:
            rich_console_error("Contact not found. Use 'add <name> <phone>' command for adding a new contact.")
            return "\n"
        except IncorrectArgumentsQuantityError as e:
            error_message = "Incorrect arguments quantity."
            error = f"{error_message} {str(e)}" if e else error_message
            rich_console_error(error)
            return "\n"
        except ContactsAreEmptyError:
            rich_console_error("Contacts are empty.")
            return "\n"
        except PhoneValidationError as e:
            rich_console_error(str(e))
            return "\n"
        except BirthdayValidationError as e:
            rich_console_error(e)
            return "\n"
        except SearchParamAreIncorrectError:
            rich_console_error("Search param is incorrect. Use 'search <search_query>' command for searching contacts.")
            return "\n"
        except ContactNotFoundAddressBook:
            rich_console_error("Contact not found in AddressBook. Please enter correct name. Use 'delete <name>'"
                    " command for removing contact")
            return "\n"
        except ContactIsAlreadyExistsError:
            rich_console_error("Contact is already registered. Use change command for update old one")
            return "\n"
        except NoteNotFoundError as e:
            rich_console_error(f"Note not found. {str(e)}" if e else "Note not found.")
            return "\n"
        except NoteAlreadyExistsError as e:
            rich_console_error(f"Note already exists. {str(e)}" if e else "Note already exists.")
            return "\n"
        except NotesListIsEmptyError:
            rich_console_error("No notes list is empty.")
            return "\n"
        except NoMatchesFoundError:
            rich_console_error("No matches found. Use 'search <search_param>' command for searching contacts.")
            return "\n"
        except Exception as e:
            rich_console_error(e)
            return "\n"
    return inner
