from datetime import datetime, date
from collections import defaultdict

from rich.panel import Panel

from cli.controllers.command import Command
from cli.exceptions.error_handler import error_handler
from cli.services.input_helper import rich_console_warning
from cli.utils.console import with_table_console
from cli.utils.constants import BIRTHDAYS_DATE_FORMAT, WEEKDAYS


class GetBirthdaysCommand(Command):
    @error_handler
    @with_table_console
    def execute(self):
        days_in_advance = self.args[0] if len(self.args) > 0 else None

        if days_in_advance is None:
            rich_console_warning("You can add days in advance. Use command 'birthdays <days_in_advance>."
                                 " Default days in advance is 7.(one week)")

        days_in_advance = int(days_in_advance) if days_in_advance is not None else 7
        today = date.today()
        birthdays = defaultdict(list)
        records = self.entry.find_all()

        for name, user in records:
            if user.birthday is not None:
                birthday_str = str(user.birthday)
                birthday = datetime.strptime(birthday_str, BIRTHDAYS_DATE_FORMAT).date()
                birthday_this_year = birthday.replace(year=today.year)

                if birthday_this_year < today:
                    birthday_this_year = birthday_this_year.replace(year=today.year + 1)

                delta_days = (birthday_this_year - today).days

                if delta_days < days_in_advance:
                    weekday = birthday_this_year.weekday()
                    if weekday in [5, 6]:
                        weekday = 0

                    weekday_name = WEEKDAYS[weekday]
                    birthdays[weekday_name].append(name)

        plural = "" if days_in_advance == 1 else "s"
        if len(birthdays) == 0:
            return f"No birthdays in next {days_in_advance} day{plural}."

        result = []

        for day in WEEKDAYS:
            if birthdays[day]:
                result.append(f"[blue]{day}: [green][italic]{', '.join((birthdays[day]))}")

        return [Panel("\n".join(result), expand=True, style="green")]
