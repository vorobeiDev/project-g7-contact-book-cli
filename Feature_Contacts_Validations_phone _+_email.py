import re

class Phone:
    def __init__(self, value):
        if not self.validate(value):
            raise ValueError(f"Некоректний номер телефону: {value}")
        self.value = value

    @staticmethod
    def validate(phone_number):
        # Припустимо, що номер має відповідати українському формату мобільного номеру: 10 цифр
        return bool(re.match(r'^\d{10}$', phone_number))

class Email:
    def __init__(self, value):
        if not self.validate(value):
            raise ValueError(f"Некоректна електронна адреса: {value}")
        self.value = value

    @staticmethod
    def validate(email_address):
        # Проста перевірка за допомогою регулярного виразу
        return bool(re.match(r'^[^@]+@[^@]+\.[^@]+$', email_address))

# Якщо потрібно, можна додати класи Name та Birthday або інші поля за потреби.

# Далі можемо використовувати ці класи для створення нового контакту:
try:
    phone = Phone("0931234567")  # Припустимо, коректний номер
    email = Email("example@example.com")  # Припустимо, коректна електронна адреса
except ValueError as e:
    print(e)
