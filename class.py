from student import Student

class ClassGroup:
    def __init__(self):
        self.students = []
        self.lowest_grade = None
        self.highest_grade = None

    def register_students(self, students):
        for student in students:
            if 0 <= student.grade <= 10:
                self.students.append(student)
                if self.lowest_grade is None or self.lowest_grade.grade > student.grade:
                    self.lowest_grade = student
                if self.highest_grade is None or self.highest_grade.grade < student.grade:
                    self.highest_grade = student

    def display_students(self):
        print('Number of students:', len(self.students))
        for student in self.students:
            print(student.display_student())
