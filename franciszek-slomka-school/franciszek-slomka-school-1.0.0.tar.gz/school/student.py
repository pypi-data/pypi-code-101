class Student:

    def __init__(self, fullname, gender, birth_year):
        self.fullname = fullname
        self.gender = gender
        self.birth_year = birth_year
    def print_details(self):
        print(f'Fullname: {self.fullname}, Gender: {self.gender}, Birth Year: {self.birth_year}')

if __name__ == "__main__":

    student1 = Student("Franek", "m", 1985)
    student1.print_details()