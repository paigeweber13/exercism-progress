DEFAULT_STUDENTS = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny',
                    'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']
PLANT_CODES = {
    'C': 'Clover',
    'G': 'Grass',
    'R': 'Radishes',
    'V': 'Violets',
}

class Garden(object):
    def __init__(self, diagram, students=DEFAULT_STUDENTS):
        self.student_responsibility_dict = {}

        students.sort()
        print(students)
        diagram_rows = diagram.split('\n')
        for i in range(0, len(diagram_rows[0]), 2):
            # Explanation:
            # 
            # students is an alphabetical array of student names
            # and contains at most n/4 elements, where n is the numver of
            # plants.
            # 
            # i goes from 0 to n/2, as it goes through each row of
            # plants in one iteration of the for loop.
            #
            # i is increased by 2 each time, as both the plant at index i and
            # at index i+1 are added in each iteration of the for loop.
            #
            # students[int(i/2)] is the key to the student_responsibility_map,
            # and contains the name of the student whose plants we are
            # currently scanning. it's i/2 because there are n/4 students and i
            # is already equal to n/2. i/2 = (n/2)/2 = n/4
            #
            # The dict is populated with an array of plant names that student
            # is in charge of. all four plants are added "simultaneously", and
            # the single-letter code is converted to a full plant name using
            # the PLANT_CODES dict.
            self.student_responsibility_dict[students[int(i/2)]] = [
                    PLANT_CODES[diagram_rows[0][i]],
                    PLANT_CODES[diagram_rows[0][i+1]], 
                    PLANT_CODES[diagram_rows[1][i]],
                    PLANT_CODES[diagram_rows[1][i+1]],
                    ]
                
    def plants(self, student_name):
        return self.student_responsibility_dict[student_name]

