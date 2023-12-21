class ContactExistsError(Exception):
    def __init__(self, message=""):
        super().__init__(message)


class IncorrectArgumentsQuantityError(Exception):
    def __init__(self, message=""):
        super().__init__(message)


class ContactNotFoundError(Exception):
    pass

class ContactsAreEmptyError(Exception):
    pass


class PhoneValidationError(Exception):
    pass


class BirthdayValidationError(Exception):
    pass


class SearchParamAreIncorrectError(Exception):
    pass


class NoMatchesFoundError(Exception):
    pass
