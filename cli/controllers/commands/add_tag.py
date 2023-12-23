from prompt_toolkit.shortcuts import input_dialog

from cli.controllers.command import Command
from cli.exceptions.error_handler import error_handler
from cli.exceptions.errors import IncorrectArgumentsQuantityError, NoteHasNotBeenChanged
from cli.utils.console import with_console


class AddTagCommand(Command):
    @error_handler
    @with_console
    def execute(self):
        if len(self.args) != 1:
            raise IncorrectArgumentsQuantityError("To add a new tag, use the 'add-tag <note_id>' command.")

        note_id = int(self.args[0])
        note = self.find_note_by_id(note_id=note_id)
        tag = input_dialog(
            title=f"Add a new tag",
            text=f"Please enter a new tag:"
        ).run()

        if tag is None:
            raise NoteHasNotBeenChanged(note_id)

        # TODO: Add check for existing tags
        note.add_tag(tag)
        return f"A new tag {tag} has been added to the note {note.title}."
