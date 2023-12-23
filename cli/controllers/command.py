from abc import ABC, abstractmethod

from cli.exceptions.errors import ContactNotFoundError, NoteNotFoundError


class Command(ABC):
    def __init__(self, args, entry):
        self.args = args or []
        self.entry = entry

    @abstractmethod
    def execute(self):
        pass

    def find_contact_by_name(self, name):
        contact = self.entry.find(name=name)
        if contact is None:
            raise ContactNotFoundError
        return contact

    def find_note_by_id(self, note_id):
        note = self.entry.find_by_id(note_id=note_id)
        if note is None:
            raise NoteNotFoundError(note_id)
        return note
