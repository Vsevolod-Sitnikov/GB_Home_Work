class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        result = str()
        for elem in self.matrix:
            result += str(elem)[1:-1] + '\n'
        return result
#В случае если матрицы одинаковой длины - проблем нет. Если же они разной длины - необходимо расширить матрицы нулями
    def __add__(self, other):
        result = []
        for i in range(len(self.matrix)):
            result.append([])
            for j in range(len(self.matrix[i])):
                try:
                    result[i].append(self.matrix[i][j] + other.matrix[i][j])
                except IndexError:
                    result[i].append(self.matrix[i][j] + 0)
                print(result[i])
        return Matrix(result)

new_elem = Matrix([[31, 32], [37, 43], [51, 86]])

new_elem_2 = Matrix([[12, 2], [68, 4], [5, 9]])

new_elem_3 = new_elem + new_elem_2

print(new_elem_3)
