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
            raise PhoneValidationError(f"Некоректний номер телефону: {value}")

    @staticmethod
    def validate(phone):
        # Припустимо, що номер має відповідати українському формату мобільного номеру: 10 цифр
        return bool(re.match(r'^\d{10}$', phone))

class Email(Field):
    def __init__(self, value):
        if self.validate(value):
                super().__init__(value)
        else:
            raise EmailValidationError(f"Некоректна електронна адреса: {value}")

    @staticmethod
    def validate(email):
        # Проста перевірка за допомогою регулярного виразу
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


class Record:
    def __init__(self, name, address=None, email=None, birthday=None):
        self.name = Name(name)
        self.phones = []
        self.birthday = Birthday(birthday) if birthday else None
        self.address = Address(address) if address else None
        self.email = Email(email) if email else None

    def __iter__(self):
        yield "name", self.name.value
        yield "phones", [phone.value for phone in self.phones]
        yield "birthday", self.birthday.value if self.birthday else None
        yield "address", self.address.value if self.address else None
        yield "email", self.email.value if self.email else None
        
    def to_dict(self):
        return dict(self)

    def add_address(self, address):
        self.address = Address(address)
    
    def add_phone(self, phone):
        self.phones.append(Phone(phone))
    
    def add_birthday(self, date):
        self.birthday = Birthday(date)

    def add_email(self, email):
        self.email = Email(email)

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                break

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        birthday = f"Birthday: {self.birthday} " if self.birthday is not None else ""
        address = f"Address: {self.address} " if self.address is not None else ""
        email = f"Email: {self.email }" if self.email is not None else ""
        return (f"Contact name: {self.name.value}; "
                f"phones: {', '.join(p.value for p in self.phones)}; " +
                f"{birthday}" +
                f"{address}" +
                f"{email}"
                )

    def __repr__(self):
        return self.__str__()
