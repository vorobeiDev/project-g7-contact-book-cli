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


class PhoneValidationError(Exception):
    pass


class EmailValidationError(Exception):
    pass


class BirthdayValidationError(Exception):
    pass


class ContactNotFoundAddressBook(Exception):
    pass


class NoteNotFoundError(Exception):
    def __init__(self, message=""):
        super().__init__(message)


class NoteAlreadyExistsError(Exception):
    pass


class NotesListIsEmptyError(Exception):
    pass


# Warnings
class ContactHasNotBeenChanged(Exception):
    def __init__(self, message=""):
        super().__init__(message)


class ContactHasNotBeenDeleted(Exception):
    def __init__(self, message=""):
        super().__init__(message)


class ContactDoesNotHaveDateOfBirth(Exception):
    def __init__(self, message=""):
        super().__init__(message)


class ContactDoesNotHavePhoneNumber(Exception):
    def __init__(self, message=""):
        super().__init__(message)


class EntryRecordsAreEmptyError(Exception):
    pass


class NoMatchesFoundError(Exception):
    pass


class ContactIsNotCreatedError(Exception):
    pass


class NoteIsNotCreatedError(Exception):
    pass


class NoteHasNotBeenChanged(Exception):
    def __init__(self, message=""):
        super().__init__(message)


class NoteHasNotBeenDeleted(Exception):
    def __init__(self, message=""):
        super().__init__(message)
