from datetime import datetime
import pickle
import os

from cli.utils.constants import BIRTHDAYS_DATE_FORMAT
from cli.exceptions.errors import PhoneValidationError, BirthdayValidationError


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if self.validate(value):
            super().__init__(value)
        else:
            raise PhoneValidationError("Phone number must have 10 digits")

    @staticmethod
    def validate(phone):
        return len(phone) == 10 and phone.isdigit()


class Birthday(Field):
    def __init__(self, value):
        if self.validate(value):
            super().__init__(value)
        else:
            raise BirthdayValidationError(f"Incorrect birthday date. Correct format is {BIRTHDAYS_DATE_FORMAT}")

    @staticmethod
    def validate(date):
        return len(date) == 10 and datetime.strptime(date, BIRTHDAYS_DATE_FORMAT)
    
class Note:
    def __init__(self, name, text):
        self.name = name
        self.text = text

    def __str__(self):
        return f"{self.name}: {self.text}"
    
class Notebook:
    def __init__(self):
        self.notes = []

    def add_note(self, name, text):
        self.notes.append(Note(name, text))

    def delete_note(self, name):
        for note in self.notes:
            if note.name == name:
                self.notes.remove(note)
                return f"Note '{name}' deleted."
        return f"Note '{name}' not found."

    def edit_note(self, name, new_text):
        for note in self.notes:
            if note.name == name:
                note.text = new_text
                return f"Note '{name}' edited."
        return f"Note '{name}' not found."

    def list_notes(self):
        return [str(note) for note in self.notes]
    
    def save_notes_to_file(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.notes, file)

    def load_notes_from_file(self, filename):
        if os.path.exists(filename) and os.path.getsize(filename) > 0:
            with open(filename, 'rb') as file:
                self.notes = pickle.load(file)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def __iter__(self):
        yield "name", self.name.value
        yield "phones", [phone.value for phone in self.phones]
        yield "birthday", self.birthday.value if self.birthday else None

    def to_dict(self):
        return dict(self)

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

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

    def add_birthday(self, date):
        self.birthday = Birthday(date)

    def __str__(self):
        birthday = f"Birthday: {self.birthday}" if self.birthday is not None else ""
        return (f"Contact name: {self.name.value}; "
                f"phones: {', '.join(p.value for p in self.phones)}; " +
                f"{birthday}"
                )

    def __repr__(self):
        return self.__str__()
