from cli.services.input_helper import rich_console, rich_console_table


def with_console(func):
    def wrapper(*args, **kwargs):
        return rich_console(func(*args, **kwargs))
    return wrapper


def with_table_console(func):
    def wrapper(*args, **kwargs):
        return rich_console_table(func(*args, **kwargs))
    return wrapper
