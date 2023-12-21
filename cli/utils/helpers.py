def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def parse_contact_input(user_input):
    args = user_input.split()
    return args


def is_match(record, query):
    for value in record.to_dict().values():
        if value is None:
            continue

        if isinstance(value, list):
            if any(query in str(item).lower() for item in value):
                return True
        elif query in str(value).lower():
            return True

    return False
