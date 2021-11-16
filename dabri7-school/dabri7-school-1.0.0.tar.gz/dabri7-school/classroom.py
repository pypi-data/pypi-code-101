class Classroom:
    def __init__(self, year_of_creation, classroom_char, students):
        self.year_of_creation = year_of_creation
        self.classroom_char = classroom_char
        self.students = students

    def show_student(self):
        for student in self.students:
            print(student.fullname)


