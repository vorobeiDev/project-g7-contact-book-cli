from rich.panel import Panel

from cli.controllers.command import Command
from cli.exceptions.error_handler import error_handler
from cli.exceptions.errors import NoMatchesFoundError, EntryRecordsAreEmptyError, \
    IncorrectArgumentsQuantityError
from cli.utils.console import with_table_console


class SearchCommand(Command):
    @error_handler
    @with_table_console
    def execute(self):
        query = " ".join(self.args)

        if len(query) == 0:
            raise IncorrectArgumentsQuantityError("Please use the 'search <search_query>'"
                                                  "command to search for contacts.")

        records = self.entry.find_all()

        if len(records) == 0:
            raise EntryRecordsAreEmptyError

        query = query.lower()
        result = {record for _, record in records if self.is_match(record, query)}

        if len(result) == 0:
            raise NoMatchesFoundError

        return [Panel(str(record), expand=True, style="green") for record in result]

    @staticmethod
    def is_match(record, query):
        for value in record.to_dict().values():
            if value is None:
                continue

            if isinstance(value, list):
                if len(value) == 0:
                    return False
                if any(query in str(item).lower() for item in value):
                    return True

            elif query in str(value).lower():
                return True

        return False
