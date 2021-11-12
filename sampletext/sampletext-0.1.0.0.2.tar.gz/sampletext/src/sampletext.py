import datetime


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def create_from_year(csl, year):
        return csl("Maksim", int(datetime.datetime.now().strftime("%Y")) - year)
