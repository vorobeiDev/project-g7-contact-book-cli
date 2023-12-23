from collections import UserDict

from cli.models.note import Note


class Notebook(UserDict):
    def add_note(self, note: Note):
        self.data[note.id] = note

    def find_by_id(self, note_id):
        return self.data.get(note_id)

    def find_all(self):
        return self.data.items()

    def find_by_name(self, name):
        return [note for note in self.data.values() if note.title == name]

    def delete(self, note_id):
        if note_id in self.data:
            del self.data[note_id]
