from student import Student
from classgroup import ClassGroup

students = [
    Student('John', 'Doe', 11),
    Student('Mary', 'Smith', 7),
    Student('Charles', 'Brown', 8),
    Student('Louise', 'White', 9),
    Student('Peter', 'Green', 6)
]

class_group = ClassGroup()
class_group.register_students(students)

class_group.display_students()
print('*' * 30)
print('Student with the lowest grade:', class_group.lowest_grade.display_student())
print('Student with the highest grade:', class_group.highest_grade.display_student())
