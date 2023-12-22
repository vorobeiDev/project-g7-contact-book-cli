from cli.exceptions.error_handler import error_handler
from cli.exceptions.errors import NoMatchesFoundError, SearchParamAreIncorrectError, ContactsAreEmptyError
from cli.models.address_book import AddressBook
from cli.models.notebook import Notebook
from cli.utils.helpers import is_match


@error_handler
def search(args, entry: AddressBook | Notebook):
    records = entry.find_all()

    if len(records) == 0:
        raise ContactsAreEmptyError

    if len(args) != 1:
        raise SearchParamAreIncorrectError

    query = args[0].lower()
    result = {record for name, record in records if is_match(record, query)}

    if len(result) == 0:
        raise NoMatchesFoundError

    return '\n'.join(str(record) for record in result)
