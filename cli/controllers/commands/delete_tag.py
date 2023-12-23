from prompt_toolkit.shortcuts import yes_no_dialog, radiolist_dialog

from cli.controllers.command import Command
from cli.exceptions.error_handler import error_handler
from cli.exceptions.errors import IncorrectArgumentsQuantityError, NoteHasNotBeenChanged
from cli.utils.console import with_console


class DeleteTagCommand(Command):
    @error_handler
    @with_console
    def execute(self):
        if len(self.args) != 1:
            raise IncorrectArgumentsQuantityError("To delete a tag, use the 'delete-tag <note_id>' command.")

        note_id = int(self.args[0])
        note = self.find_note_by_id(note_id=note_id)
        target_tag = self.get_tag_for_deleting(note.tags, note_id)

        result = yes_no_dialog(
            title=f"Delete tag from the note {note.title}",
            text=f"Do you want to delete tag '{target_tag}' from the note '{note.title}'?",
            yes_text="Yes, delete!"
        ).run()

        if result is False:
            raise NoteHasNotBeenChanged(note_id)

        note.delete_tag(target_tag)
        return f"Tag has been deleted from the note '{note.title}'."

    @staticmethod
    def get_tag_for_deleting(tags, id):
        values = [(str(tag), str(tag)) for tag in tags]
        target_tag = radiolist_dialog(
            title="Delete Tag",
            text="Which tag do you want to delete?",
            values=values
        ).run()

        if target_tag is None:
            raise NoteHasNotBeenChanged(id)

        return target_tag
