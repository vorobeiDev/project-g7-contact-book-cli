class ContactExistsError(Exception):
    def __init__(self, message=""):
        super().__init__(message)


class IncorrectArgumentsQuantityError(Exception):
    def __init__(self, message=""):
        super().__init__(message)


class ContactNotFoundError(Exception):
    pass


class ContactIsAlreadyExistsError(Exception):
    pass


class ContactsAreEmptyError(Exception):
    pass


class PhoneValidationError(Exception):
    pass

class EmailValidationError(Exception):
    pass

class BirthdayValidationError(Exception):
    pass


class SearchParamAreIncorrectError(Exception):
    pass


class NoMatchesFoundError(Exception):
    pass

class ContactNotFoundAddressBook(Exception):
    pass


class NoteNotFoundError(Exception):
    pass

class NoteAlreadyExistsError(Exception):
    pass
