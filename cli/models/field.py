import re
from datetime import datetime

from cli.utils.constants import BIRTHDAYS_DATE_FORMAT
from cli.exceptions.errors import PhoneValidationError, BirthdayValidationError, EmailValidationError


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Address(Field):
    def __init__(self, value):
        super().__init__(value)


class Phone(Field):
    def __init__(self, value):
        if self.validate(value):
            super().__init__(value)
        else:
            raise PhoneValidationError(f"Incorrect phone number: {value}")

    @staticmethod
    def validate(phone):
        """Validation of phone number"""
        return bool(re.match(r'^\d{10}$', phone))


class Email(Field):
    def __init__(self, value):
        if self.validate(value):
            super().__init__(value)
        else:
            raise EmailValidationError(f"Incorrect email: {value}")

    @staticmethod
    def validate(email):
        """Validation of email address"""
        return bool(re.match(r'^[^@]+@[^@]+\.[^@]+$', email))


class Birthday(Field):
    def __init__(self, value):
        if self.validate(value):
            super().__init__(value)
        else:
            raise BirthdayValidationError(f"Incorrect birthday date. Correct format is {BIRTHDAYS_DATE_FORMAT}")

    @staticmethod
    def validate(date):
        return len(date) == 10 and datetime.strptime(date, BIRTHDAYS_DATE_FORMAT)


class Title(Field):
    pass


class Description(Field):
    pass


class Tag(Field):
    pass
