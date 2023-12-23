from prompt_toolkit.shortcuts import input_dialog

from cli.controllers.command import Command
from cli.exceptions.error_handler import error_handler
from cli.exceptions.errors import IncorrectArgumentsQuantityError, NoteIsNotCreatedError
from cli.models.note import Note
from cli.utils.console import with_console


class AddNoteCommand(Command):
    @error_handler
    @with_console
    def execute(self):
        if len(self.args) != 0:
            raise IncorrectArgumentsQuantityError("To add a new note, use 'add-note' command.")

        title = input_dialog(
            title="Create a new Note",
            text="Please enter a title for a new Note:"
        ).run()

        if title is None:
            raise NoteIsNotCreatedError

        note_information = ["description", "tag"]

        new_note = Note(title=title)

        for key in note_information:
            value = input_dialog(
                title=f"Add a {key}",
                text=f"Please enter a note {key}:",
                ok_text="Add",
                cancel_text="Skip"
            ).run()

            if value is None:
                continue
            else:
                if key == "description":
                    new_note.add_description(value)
                if key == "tag":
                    new_note.add_tag(value)

        self.entry.add_note(note=new_note)
        return f"A new note with id {new_note.id} and title '{new_note.title}' has been created.!"
