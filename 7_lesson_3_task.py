class Cell:

    def __init__(self, alveola):
        self.alveola = alveola

    def __add__(self, other):
        return Cell(self.alveola + other.alveola)

    def __sub__(self, other):
        if self.alveola - other.alveola > 0:
            return Cell(self.alveola - other.alveola)
        else:
            print("Разниза при вычитании меньше 0")

    def __mul__(self, other):
        return Cell(self.alveola * other.alveola)

    def __truediv__(self, other):
        return Cell(int(self.alveola / other.alveola))

#нужно было экранировать \n или нет? не совсем понял из задания
    def make_order(self, alveola_count):
        result = ('*' * alveola_count + '\n') * (self.alveola // alveola_count) + ('*' * (self.alveola % alveola_count))
        print(result)

nutrion_1 = Cell(123)

nutrion_2 = Cell(89)

nutrion_3 = nutrion_1 + nutrion_2

nutrion_4 = nutrion_1 - nutrion_2

nutrion_5 = nutrion_1 * nutrion_2

nutrion_6 = nutrion_1 / nutrion_2

print(nutrion_1.alveola)

print(nutrion_2.alveola)

print(nutrion_3.alveola)

print(nutrion_4.alveola)

print(nutrion_5.alveola)

print(nutrion_6.alveola)

nutrion_1.make_order(10)
