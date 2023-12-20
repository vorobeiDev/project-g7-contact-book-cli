from datetime import datetime

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
    
# Додано клас Note. Його ведено для подання нотатки, пов'язаної з контактом, успадковується від існуючого класу Field.
class Note(Field):
    def __init__(self, value):
        super().__init__(value)

# Додано виняток NoteNotFoundError, він виникає при спробі виконати операцію з неіснуючою нотаткою.
class NoteNotFoundError(Exception):
    pass


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        # Додано атрибут нотаток для збереження списку нотаток, пов'язаних із контактом
        self.notes = []

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

    # Додані методи (add_note, remove_note, edit_note, find_note) для виконання операцій над нотатками
    def add_note(self, note):
        self.notes.append(Note(note))

    def remove_note(self, note):
        if note in [n.value for n in self.notes]:
            self.notes = [n for n in self.notes if n.value != note]
        else:
            raise NoteNotFoundError(f"Note with name '{note}' not found.")

    def edit_note(self, old_note, new_note):
        for note in self.notes:
            if note.value == old_note:
                note.value = new_note
                break
        else:
            raise NoteNotFoundError(f"Note with name '{old_note}' not found.")

    def find_note(self, note):
        for n in self.notes:
            if n.value == note:
                return n
        return None

    # Оновлено метод __str__, який включає відображення нотаток під час друку контакту
    def __str__(self):
        birthday = f"Birthday: {self.birthday}" if self.birthday is not None else ""
        notes = f"Notes: {', '.join(note.value for note in self.notes)}" if self.notes else ""
        return (f"Contact name: {self.name.value}; "
                f"phones: {', '.join(p.value for p in self.phones)}; " +
                f"{birthday} {notes}"
                )

    def __repr__(self):
        return self.__str__()
