def fun_for_division(a, b):
    """
    Функция делит переменную a на переменную b
    :param a: целое число, введеное пользователем
    :param b: целое число, введеное пользователем
    :return: число типа float. При b = 0 возвращается сообщение 'На ноль делить нельзя'
    """
    try:
        return a / b
    except ZeroDivisionError:
        return str('На ноль делить нельзя')


var_a = None

var_b = None

#добавил исключения для проверки типа данных вводимой переменной

while not var_a:
    try:
        var_a = float(input('Введите значение a: '))
    except ValueError:
        print('Тип введенного значения не равен float. Попробуйте повторить')


while not var_b:
    try:
        var_b = float(input('Введите значение b: '))
    except ValueError:
        print('Тип введенного значения не равен float. Попробуйте повторить')


print(fun_for_division(var_a, var_b))
