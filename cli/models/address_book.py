from collections import UserDict
from cli.models.record import Record


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def find_all(self):
        return self.data.items()

    def delete(self, name):
        if name in self.data:
            del self.data[name]
