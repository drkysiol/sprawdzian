class User:
    def __init__(self, id, first_name, last_name, birth_year, group):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.group = group

    @property
    def age(self):
        return 2024 - self.birth_year
