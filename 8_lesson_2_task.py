class MyException(Exception):

    def __init__(self, text):
        self.text = text
var_a = int(input("Введите делимое: "))

var_b = int(input("Введите делитель: "))

try:
    if var_b == 0:
        raise MyException("Делитель не должен быть равен 0")
    print(var_a / var_b)

except MyException as err:
    print(err)
