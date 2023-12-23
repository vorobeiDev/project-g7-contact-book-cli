from prompt_toolkit.shortcuts import yes_no_dialog

from cli.controllers.command import Command
from cli.exceptions.error_handler import error_handler
from cli.exceptions.errors import IncorrectArgumentsQuantityError, NoteHasNotBeenDeleted
from cli.utils.console import with_console


class DeleteNoteCommand(Command):
    @error_handler
    @with_console
    def execute(self):
        if len(self.args) != 1:
            raise IncorrectArgumentsQuantityError("To delete a note, use the 'delete-note <id>' command.")

        note_id = int(self.args[0])
        note = self.find_note_by_id(note_id=note_id)

        result = yes_no_dialog(
            title="Delete a note",
            text=f"Do you want to delete a note with id '{note_id} and title {note.title}'?",
            yes_text="Yes, delete!"
        ).run()

        if result is False:
            raise NoteHasNotBeenDeleted(note_id)

        self.entry.delete(note_id)
        return f"The note with id {note_id} and title {note.title} has been deleted."
