from cli.models.field import Name, Address, Birthday, Phone, Email


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.address = None
        self.email = None

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

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

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

    def change_birthday(self, birthday):
       self.birthday = Birthday(birthday)

    def change_email(self, email):
        self.email = Email(email)

    def change_name(self, new_name):
        self.name = Name(new_name)

    def __str__(self):
        phones = f"\nPhones: {', '.join(p.value for p in self.phones)}; " if len(self.phones) > 0 else ""
        birthday = f"\nBirthday: {self.birthday}; " if self.birthday is not None else ""
        address = f"\nAddress: {self.address}; " if self.address is not None else ""
        email = f"\nEmail: {self.email}; " if self.email is not None else ""
        return (f"Contact name: {self.name.value}; "
                f"{phones}" +
                f"{birthday}" +
                f"{address}" +
                f"{email}"
                "\n"
                )

    def __repr__(self):
        return self.__str__()
