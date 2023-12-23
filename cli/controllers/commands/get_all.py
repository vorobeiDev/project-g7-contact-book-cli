from rich.panel import Panel

from cli.controllers.command import Command
from cli.exceptions.error_handler import error_handler
from cli.exceptions.errors import IncorrectArgumentsQuantityError, EntryRecordsAreEmptyError
from cli.utils.console import with_table_console


class GetAllCommand(Command):
    @error_handler
    @with_table_console
    def execute(self):
        if len(self.args) != 0:
            raise IncorrectArgumentsQuantityError()

        records = self.entry.find_all()

        if len(records) == 0:
            raise EntryRecordsAreEmptyError()

        return [Panel(str(record), expand=True, style="green") for _, record in records]
