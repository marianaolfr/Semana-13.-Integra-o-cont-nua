class Student:
    def __init__(self, first_name, last_name, grade):
        self.first_name = first_name
        self.last_name = last_name
        self.grade = grade

    def display_student(self):
        return f"Student: {self.first_name} {self.last_name} - Grade: {self.grade}"
