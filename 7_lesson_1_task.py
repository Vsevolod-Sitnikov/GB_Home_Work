class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        result = str()
        for elem in self.matrix:
            result += str(elem)[1:-1] + '\n'
        return result
'''
В случае если матрицы одинаковой длины - проблем нет. Если же они разной длины - сложение не возможно с математической точки зрения. Для примера сделал if...else условие.
В первом случае вызываю ошибку, во втором просто вызываю print()
'''
    def __add__(self, other):
        result = []
        if len(self.matrix) == len(other.matrix):
            for i in range(len(self.matrix)):
                if len(self.matrix[i]) == len(other.matrix[i]):
                    result.append([])
                    for j in range(len(self.matrix[i])):
                        result[i].append(self.matrix[i][j] + other.matrix[i][j])
                else:
                    raise ValueError("Матрицы разных размеров")
        else:
            print("Сложение не возможно, матрицы разной длины")
        return Matrix(result)

new_elem = Matrix([[31, 32], [37, 43], [51, 86, 5]])

new_elem_2 = Matrix([[12, 2], [68, 4], [5, 9]])

new_elem_3 = new_elem + new_elem_2

print(new_elem_3)
