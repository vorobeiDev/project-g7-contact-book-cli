from collections import UserDict
from datetime import datetime, timedelta


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def find_all(self):
        return self.data.items()

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def get_birthdays_soon(self, days_in_advance):
        # Метод для отримання контактів з днями народження, що наближаються
        today = datetime.now()  # Поточна дата
        upcoming_birthdays = {}  # Словник для зберігання майбутніх днів народження

        # Проходимося по всіх записах в адресній книзі
        for name, record in self.data.items():
            # Перевіряємо, чи є у запису дата народження
            if record.birthday:
                # Конвертуємо рядок дати народження в об'єкт datetime
                birthday_date = datetime.strptime(record.birthday.value, '%d.%m.%Y')
                # Оновлюємо рік дня народження до поточного року
                current_year_birthday = birthday_date.replace(year=today.year)
                # Обчислюємо різницю в днях між поточною датою та днем народження
                delta_days = (current_year_birthday - today).days

                # Якщо день народження вже пройшов, враховуємо наступний рік
                if delta_days < 0:
                    current_year_birthday = current_year_birthday.replace(year=today.year + 1)
                    delta_days = (current_year_birthday - today).days

                # Якщо день народження в межах вказаної кількості днів, додаємо до словника
                if 0 <= delta_days <= days_in_advance:
                    upcoming_birthdays.setdefault(delta_days, []).append(name)

        return upcoming_birthdays  # Повертаємо словник днів народження