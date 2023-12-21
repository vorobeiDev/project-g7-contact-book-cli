from cli.exceptions.error_handler import error_handler
from cli.exceptions.errors import IncorrectArgumentsQuantityError, NoteAlreadyExistsError, NoteNotFoundError, \
    NotesListIsEmptyError
from cli.models.note import Note
from cli.models.notebook import Notebook
from cli.utils.helpers import parse_question_input


@error_handler
def add_note(args, notebook: Notebook):
    if len(args) < 1:
        raise IncorrectArgumentsQuantityError("To add a note, use 'add-note <title>' command.")

    title = " ".join(args)
    new_note = Note(title=title)

    note_information = ["description"]

    for key in note_information:
        user_input = input(f"Do you want to add a {key}? (n/no - for skip): ")
        args = parse_question_input(user_input)

        if args[0].lower() in ["n", "no"]:
            continue
        else:
            value = " ".join(args)
            if key == "description":
                new_note.description = value

    notebook.add_note(new_note)
    return f"New note with id {new_note.id} added!"


@error_handler
def get_all_notes(notebook: Notebook):
    notes = notebook.find_all()
    if len(notes) == 0:
        raise NotesListIsEmptyError
    return "\n".join([str(note) for _id, note in notes])


@error_handler
def edit_note(args, notebook: Notebook):
    if len(args) != 1:
        raise IncorrectArgumentsQuantityError("To edit a note, use 'edit-note <id>' command.")
    _id = args[0]
    note = notebook.find_by_id(_id=int(_id))
    if note is None:
        raise NoteNotFoundError(f"Note with id {_id} does not found")

    note_information = ["title", "description"]

    for key in note_information:
        user_input = input(f"Do you want to update a {key}? (n/no - for skip): ")
        args = parse_question_input(user_input)
        if args[0].lower() in ["n", "no"]:
            continue
        else:
            value = " ".join(args)
            if key == "title":
                note.edit_title(new_title=value)
            elif key == "description":
                note.edit_description(new_description=value)

    return f"Note title with id {_id} was updated."


@error_handler
def delete_note(args, notebook: Notebook):
    if len(args) != 1:
        raise IncorrectArgumentsQuantityError("To delete a note, use 'delete-note <id>' command.")

    _id = args[0]
    note = notebook.find_by_id(_id=int(_id))
    if note is None:
        raise NoteNotFoundError(f"Note with id {_id} does not found")

    notebook.delete(_id=int(_id))
    return f"Note with id {_id} was deleted."
