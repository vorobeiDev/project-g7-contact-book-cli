from prompt_toolkit.shortcuts import yes_no_dialog

from cli.exceptions.error_handler import error_handler
from cli.exceptions.errors import IncorrectArgumentsQuantityError, NoteAlreadyExistsError, NoteNotFoundError, \
    NotesListIsEmptyError
from cli.models.note import Note
from cli.models.notebook import Notebook
from cli.services.input_helper import answer_prompt_handler
from cli.utils.helpers import parse_question_input


@error_handler
def add_note(args, notebook: Notebook):
    if len(args) < 1:
        raise IncorrectArgumentsQuantityError("To add a note, use 'add-note <title>' command.")

    title = " ".join(args)
    new_note = Note(title=title)

    note_information = ["description", "tag"]

    for key in note_information:
        user_input = answer_prompt_handler(f"Do you want to add a {key}? (n/no - for skip): ")
        args = parse_question_input(user_input)

        if args[0].lower() in ["n", "no"]:
            continue
        else:
            value = " ".join(args)
            if key == "description":
                new_note.add_description(value)
            if key == "tag":
                new_note.add_tag(value)

    notebook.add_note(new_note)
    return f"New note with id {new_note.id} added!"


@error_handler
def get_all_notes(notebook: Notebook):
    notes = notebook.find_all()
    if len(notes) == 0:
        raise NotesListIsEmptyError
    return "\n".join([str(note) for _, note in notes])


@error_handler
def get_all_notes_object(notebook: Notebook):
    notes = notebook.find_all()
    return notes


@error_handler
def get_notes_content(note):
    """Extract text from user dict."""
    key, value = note
    value = str(value)

    parts = value.split(';')

    # Initialize variables to store extracted keys and values
    _id = None
    title = None
    description = None
    tags = None

    for part in parts:
        # Split each part into key and value based on the ':'
        key_value = part.split(':')

        # Clean up whitespace and assign the key-value pairs accordingly
        if len(key_value) == 2:
            key = key_value[0].strip()
            val = key_value[1].strip()

            if key == 'ID':
                _id = val
            if key == 'Title':
                title = val
            elif key == 'Description':
                description = val
            elif key == 'Tags':
                tags = val

    # Print or use the extracted keys and values
    return f"[b]{_id}[/b]\n[white]Title: [yellow]{title}\n[white]Description: [yellow]{description}\n[white]Tags: [yellow]{tags}\n"


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
        user_input = answer_prompt_handler(f"Do you want to update a {key}? (n/no - for skip): ")
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

    result = yes_no_dialog(
        title="Delete note",
        text=f"Do you want to delete note '{note.title.value}'?").run()

    if result:
        notebook.delete(_id=int(_id))
        return f"Note with id {_id} was deleted."
    else:
        return f"Note '{note.title.value}' doesn't deleted!"


@error_handler
def add_tag(args, notebook: Notebook):
    if len(args) < 2:
        raise IncorrectArgumentsQuantityError("To add a tag, use 'add-tag <id> <tag>' command.")
    _id, *tags = args
    note = notebook.find_by_id(_id=int(_id))
    if note is None:
        raise NoteNotFoundError(f"Note with id {_id} does not found")

    note.add_tag(" ".join(tags))
    return f"Tag(s) added to note with id {_id}."


@error_handler
def delete_tag(args, notebook: Notebook):
    if len(args) < 2:
        raise IncorrectArgumentsQuantityError("To delete a tag, use 'delete-tag <id> <tag>' command.")
    _id, *tags = args
    note = notebook.find_by_id(_id=int(_id))
    if note is None:
        raise NoteNotFoundError(f"Note with id {_id} does not found")

    note.delete_tag(" ".join(tags))
    return f"Tag(s) deleted from note with id {_id}."
