import re

class Matrix(object):
    matrix = []

    def __init__(self, matrix_string):
        self.matrix = []
        i = 0
        self.matrix.append([])
        while(len(matrix_string) > 0):
            # print("matrix string:", matrix_string)
            # print("matrix: ", self.matrix)
            # print("i:", i)
            match = re.match(r'\d+', matrix_string)
            if match:
                self.matrix[i].append(int(match.group()))
                matrix_string = matrix_string[match.span()[1]:]
                continue

            match = re.match(r' ', matrix_string)
            if match:
                matrix_string = matrix_string[match.span()[1]:]
                continue

            match = re.match(r'\n', matrix_string)
            if match:
                matrix_string = matrix_string[match.span()[1]:]
                self.matrix.append([])
                i += 1
                continue

            

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        print("matrix: ", self.matrix)
        index = index - 1
        column_list = []
        for row in self.matrix:
            column_list.append(row[index])
        return column_list
