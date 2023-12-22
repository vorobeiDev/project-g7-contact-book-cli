from cli.models.field import Title, Description


class Note:
    counter = 1

    def __init__(self, title):
        self.id = type(self).counter
        self.title = Title(title)
        self.description = None
        self.tags = []
        type(self).counter += 1

    def __str__(self):
        tags_str = f": {', '.join(map(str, self.tags))}" if self.tags else ""
        return f"{self.id}: {self.title}{tags_str}: {self.description}"

    def add_description(self, description):
        self.description = Description(description)

    def edit_description(self, new_description):
        self.description = Description(new_description)

    def edit_title(self, new_title):
        self.title = Title(new_title)

    def add_tag(self, tag):
        self.tags.append(tag)

    def delete_tag(self, tag):
        if tag in self.tags:
            self.tags.remove(tag)