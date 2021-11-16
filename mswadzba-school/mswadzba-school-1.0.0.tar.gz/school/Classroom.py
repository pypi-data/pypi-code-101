class Classroom:

    def __init__(self, class_year, classroom, students):
        self.year_of_creation = class_year
        self.classroom_char = classroom
        self.students = students

    def show_students(self):
        for student in self.students:
            print(student.fullname)


