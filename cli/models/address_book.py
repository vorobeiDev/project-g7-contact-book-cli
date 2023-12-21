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
