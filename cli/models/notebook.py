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