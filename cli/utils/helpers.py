def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def parse_question_input(user_input):
    args = user_input.split()
    return args
