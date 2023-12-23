from cli.exceptions.errors import ContactExistsError, ContactNotFoundError, \
    ContactIsAlreadyExistsError, NoteNotFoundError, \
    NoteAlreadyExistsError, NotesListIsEmptyError, \
    IncorrectArgumentsQuantityError, EntryRecordsAreEmptyError, PhoneValidationError, BirthdayValidationError, \
    NoMatchesFoundError, ContactHasNotBeenChanged, ContactHasNotBeenDeleted, \
    ContactDoesNotHaveDateOfBirth, ContactDoesNotHavePhoneNumber, ContactIsNotCreatedError, NoteIsNotCreatedError, \
    NoteHasNotBeenChanged, NoteHasNotBeenDeleted
from cli.services.input_helper import rich_console_error, rich_console_warning


def error_handler(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ContactExistsError as e:
            error_message = "Contact already exists."
            error = f"{error_message} {str(e)}" if e else error_message
            rich_console_error(error)
        except ContactNotFoundError:
            rich_console_error("Contact not found. Use 'add' command for adding a new contact.")
        except IncorrectArgumentsQuantityError as e:
            error_message = "Incorrect arguments quantity."
            error = f"{error_message} {str(e)}" if e else error_message
            rich_console_error(error)
        except PhoneValidationError as e:
            rich_console_error(str(e))
        except BirthdayValidationError as e:
            rich_console_error(e)
        except ContactIsAlreadyExistsError:
            rich_console_error("Contact is already registered. Use change command for update old one")
        except NoteNotFoundError as note_id:
            rich_console_error(f"Note with id {note_id} does not found.")
        except NoteAlreadyExistsError as e:
            rich_console_error(f"Note already exists. {str(e)}" if e else "Note already exists.")
        except NotesListIsEmptyError:
            rich_console_error("No notes list is empty.")
        except ContactHasNotBeenChanged as name:
            rich_console_warning(f"Contact '{name}' has not been changed!")
        except ContactHasNotBeenDeleted as name:
            rich_console_warning(f"Contact '{name}' has not been deleted!")
        except ContactDoesNotHaveDateOfBirth as name:
            rich_console_warning(f"Contact '{name}' does not have a date of birth.")
        except ContactDoesNotHavePhoneNumber as name:
            rich_console_warning(f"Contact '{name}' does not have a phone number.")
        except EntryRecordsAreEmptyError:
            rich_console_warning("List is empty.")
        except NoMatchesFoundError:
            rich_console_warning("No matches found.")
        except ContactIsNotCreatedError:
            rich_console_warning("A new Contact has not been created.")
        except NoteIsNotCreatedError:
            rich_console_warning("A new Note has not been created.")
        except NoteHasNotBeenChanged as note_id:
            rich_console_warning(f"Note with id '{note_id}' has not been changed!")
        except NoteHasNotBeenDeleted as note_id:
            rich_console_warning(f"Note with id '{note_id}' has not been deleted!")
        except Exception as e:
            rich_console_error(e)
    return inner
