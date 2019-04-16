class Student(object):
    def __init__(self, name = '', grade = 0):
        self.name = name
        self.grade = grade
    
    def __lt__(self, other):
        if self.grade < other.grade:
            return True
        elif self.grade == other.grade and self.name < other.name:
            return True
        else:
            return False