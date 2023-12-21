from .errors import ContactExistsError, ContactNotFoundError, \
    IncorrectArgumentsQuantityError, ContactsAreEmptyError, PhoneValidationError, \
    BirthdayValidationError, SearchParamAreIncorrectError, NoMatchesFoundError, \
    ContactIsAlreadyExistsError, ContactNotFoundAddressBook, NoteNotFoundError, \
    NoteAlreadyExistsError, NotesListIsEmptyError


def error_handler(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ContactExistsError as e:
            error_message = "Contact already exists."
            return f"{error_message} {str(e)}" if e else error_message
        except ContactNotFoundError:
            return "Contact not found. Use 'add <name> <phone>' command for adding a new contact."
        except IncorrectArgumentsQuantityError as e:
            error_message = "Incorrect arguments quantity."
            return f"{error_message} {str(e)}" if e else error_message
        except ContactsAreEmptyError:
            return "Contacts are empty."
        except PhoneValidationError as e:
            return e
        except BirthdayValidationError as e:
            return e
        except SearchParamAreIncorrectError:
            return "Search param is incorrect. Use 'search <search_query>' command for searching contacts."
        except NoMatchesFoundError:
            return "No matches found. Use 'search <search_query>' command for searching contacts."
        except ContactNotFoundAddressBook:
            return ("Contact not found in AddressBook. Please enter correct name. Use 'delete <name>'"
                    " command for removing contact")
        except ContactIsAlreadyExistsError:
            return "Contact is already registered. Use change command for update old one"
        except NoteNotFoundError as e:
            return f"Note not found. {str(e)}" if e else "Note not found."
        except NoteAlreadyExistsError as e:
            return f"Note already exists. {str(e)}" if e else "Note already exists."
        except NotesListIsEmptyError:
            return "No notes list is empty"
        # except Exception as e:
        #     return e
    return inner
