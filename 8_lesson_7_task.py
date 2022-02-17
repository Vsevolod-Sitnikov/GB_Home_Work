class ComplexNumber:
    def __init__(self, real_number,imaginary_number):
        self.real_number = real_number
        self.imaginary_number = imaginary_number

    def __add__(self, other):
        real_number = self.real_number + other.real_number
        imaginary_number = self.imaginary_number + other.imaginary_number
        print(f'{real_number}+j{imaginary_number}')
        return ComplexNumber(real_number, imaginary_number)

    def __mul__(self, other):
        real_number = self.real_number * other.real_number - self.imaginary_number * other.imaginary_number
        imaginary_number = self.imaginary_number * other.real_number + self.real_number * other.imaginary_number
        print(f'{real_number}+j{imaginary_number}')
        return ComplexNumber(real_number, imaginary_number)


number_one = ComplexNumber(15, 10)
number_two = ComplexNumber(5, -3)

number_three = number_one + number_two
number_four = number_one * number_two

