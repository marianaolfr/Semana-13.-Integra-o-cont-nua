import unittest
from student import Student
from class_group import ClassGroup


class ClassGroupTest(unittest.TestCase):

    def setUp(self):
        print('Test', self._testMethodName, 'is running...')
        self.students = [
            Student('John', 'Doe', 11),
            Student('Mary', 'Smith', 7),
            Student('Charles', 'Brown', 8),
            Student('Louise', 'White', 9),
            Student('Anthony', 'Green', 6)
        ]
        self.class_group = ClassGroup()
        self.class_group.register_students(self.students)

    def tearDown(self):
        print('Test', self._testMethodName, 'finished.')

    def test_highest_grade(self):
        self.assertEqual(
            9, 
            self.class_group.highest_grade.grade, 
            'Error finding the highest grade'
        )

    def test_lowest_grade(self):
        self.assertEqual(
            6, 
            self.class_group.lowest_grade.grade, 
            'Error finding the lowest grade'
        )

    def test_grade_range(self):
        self.assertTrue(
            0 < self.class_group.lowest_grade.grade <= 10,
            'Error verifying grade range'
        )


if __name__ == "__main__":
    unittest.main()
