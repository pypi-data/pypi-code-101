"""
Napisz bibliotekę i wrzuć ją do PYPI realizujacą abstrakcję szkoły podstawowej.
1. Napisz klasę Student reprezentującą ucznia w szkole. Uczeń posiada następujące atrybuty:
    * fullname - imie i nazwisko
    * gender - M/F
    * birth_year
2. Napisz klasę Classroom reprezentującą klasę, do której uczęszczają uczniowie. Posiada następujące atrybuty:
    * year_of_creation - rok utworzenia klasy
    * classroom_char - odpowiednio a, b, c itd.
    * students - lista uczniów uczeszczających do danej klasy
    Posiada metode show_students() wyświetlającą wszystkich uczniów

    Paczka powinna się nazywa w konwencji <imie_nazwisko>-school.
"""
from student import Student


class Classroom:

    def __init__(self, year_of_creation, classroom_char, students=[]):
        self.year_of_creation = year_of_creation
        self.classroom_char = classroom_char
        self.students = students

    def show_students(self):
        for student in self.students:
            student.print_details()


