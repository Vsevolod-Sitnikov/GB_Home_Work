def my_func_1(a, b):
    """
    Функция возводит в степень при помощи цикла
    """
    end_result = a
    if b > 0:
        while b > 1:
            b -= 1
            end_result *= a
        return end_result
    elif b < 0:
        while b < 1:
            end_result /= a
            b += 1
        return end_result
    else:
        return 0


def my_func(a, b):
    """
    Упрощенная функция, возведение в степень происходит при помощи оператора **
    """
    return a ** b


var_a = int(input('Введите значение a: '))

var_b = int(input('Введите значение b: '))

print("Значение, полученное функцией my_func")
print(my_func(var_a, var_b))

print("Значение, полученное функцией my_func_1")
print(my_func_1(var_a, var_b))
