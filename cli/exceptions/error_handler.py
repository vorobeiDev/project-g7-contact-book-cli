from .errors import ContactExistsError, ContactNotFoundError, \
    IncorrectArgumentsQuantityError, ContactsAreEmptyError, PhoneValidationError, BirthdayValidationError, \
    SearchParamAreIncorrectError, NoMatchesFoundError, ContactIsAlreadyExistsError


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
            return "Search param is incorrect. Use 'search <search_param>' command for searching contacts."
        except NoMatchesFoundError:
            return "No matches found. Use 'search <search_param>' command for searching contacts."
        except ContactIsAlreadyExistsError:
            return "Contact is already registered. Use change command for update old one"
        except Exception as e:
            return e
    return inner
