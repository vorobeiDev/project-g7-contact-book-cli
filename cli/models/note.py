from cli.models.field import Title, Description


class Note:
    counter = 1

    def __init__(self, title):
        self.id = type(self).counter
        self.title = Title(title)
        self.description = None
        type(self).counter += 1

    def __str__(self):
        return f"{self.id}: {self.title}: {self.description}"

    def add_description(self, description):
        self.description = Description(description)

    def edit_description(self, new_description):
        self.description = Description(new_description)

    def edit_title(self, new_title):
        self.title = Title(new_title)