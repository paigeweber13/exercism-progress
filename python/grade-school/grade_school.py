from student import Student

class School(object):
    def __init__(self):
        self.students = []

    def add_student(self, name, grade):
        self.students.append(Student(name, grade))
        self.students.sort()

    def roster(self):
        result = []
        for student in self.students:
            result.append(student.name)
        return result

    def grade(self, grade_number):
        result = []
        for student in self.students:
            if student.grade == grade_number:
                result.append(student.name)
        return result
