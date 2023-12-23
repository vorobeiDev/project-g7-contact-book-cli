from prompt_toolkit.shortcuts import radiolist_dialog, input_dialog

from cli.controllers.command import Command
from cli.exceptions.error_handler import error_handler
from cli.exceptions.errors import IncorrectArgumentsQuantityError, NoteHasNotBeenChanged
from cli.utils.console import with_console


class ChangeNoteCommand(Command):
    @error_handler
    @with_console
    def execute(self):
        if len(self.args) != 1:
            raise IncorrectArgumentsQuantityError("To change a note, use 'change-note <id>' command.")

        # TODO: Add correct check for int() conversion
        note_id = int(self.args[0])
        note = self.find_note_by_id(note_id=note_id)

        key = radiolist_dialog(
            title="Change a note",
            text="Which param do you want to change?",
            values=[
                ("title", "Contact title"),
                ("description", "Note description"),
            ]
        ).run()

        if key is None:
            raise NoteHasNotBeenChanged(note_id)

        if key == "title":
            new_title = self.get_new_value(key, note_id)
            note.change_title(new_title=new_title)
        if key == "description":
            new_description = self.get_new_value(key, note_id)
            note.change_description(new_description=new_description)

        return f"The note with id '{note.id}' has been changed."

    @staticmethod
    def get_new_value(key, note_id):
        value = input_dialog(
            title=f"Change a note {key}",
            text=f"Please enter a new note {key}:"
        ).run()

        if value is None:
            raise NoteHasNotBeenChanged(note_id)

        return value
