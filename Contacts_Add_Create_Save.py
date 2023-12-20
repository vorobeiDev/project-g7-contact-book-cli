from datetime import datetime, timedelta
from collections import UserDict
import pickle
import re

class Field:
    def __init__(self, value):
        self.value = value

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Номер телефону повинен складатися з 10 цифр")
        super().__init__(value)

class Address(Field):
    pass

class Email(Field):
    def __init__(self, value):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
            raise ValueError("Некоректна електронна пошта")
        super().__init__(value)

class Birthday(Field):
    def __init__(self, value):
        try:
            datetime.strptime(value, '%d.%m.%Y')
        except ValueError:
            raise ValueError("Дата народження має бути у форматі DD.MM.YYYY")
        super().__init__(value)

class Record:
    def __init__(self, name, address=None, email=None, birthday=None):
        self.name = Name(name)
        self.address = Address(address) if address else None
        self.email = Email(email) if email else None
        self.birthday = Birthday(birthday) if birthday else None
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    # Методи для редагування, видалення та інші

class AddressBook(UserDict):
    # Методи AddressBook для роботи з записами

    def save_to_disk(self, filename='address_book.pkl'):
        with open(filename, 'wb') as file:
            pickle.dump(self.data, file)

    def load_from_disk(self, filename='address_book.pkl'):
        try:
            with open(filename, 'rb') as file:
                self.data = pickle.load(file)
        except FileNotFoundError:
            print("Файл не знайдено. Створено нову адресну книгу.")

class MyBot:
    def __init__(self):
        self.book = AddressBook()
        self.book.load_from_disk()

    def add_contact(self, args):
        try:
            name, address, phone, email, birthday = args
            contact = Record(name, address, email, birthday)
            contact.add_phone(phone)
            self.book[name] = contact
            return f"Контакт {name} додано."
        except ValueError as e:
            return str(e)

    # Інші методи для обробки команд

    def main(self):
        print("Ласкаво просимо до бота-помічника!")
        while True:
            user_input = input("Введіть команду: ")
            command, args = self.parse_input(user_input)
            result = self.process_command(command, args)
            print(result)

if __name__ == "__main__":
    bot = MyBot()
    bot.main()
