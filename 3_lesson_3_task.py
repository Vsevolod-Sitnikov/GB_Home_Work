def my_func (a, b, c):
    """
    Возвращает информацию о сумме двух наибольших чисел из трёх введеных
    """
    new_list = [a, b, c]
    new_list.sort()
    return new_list[1] + new_list[2]


var_a = int(input('Введите переменную a: '))

var_b = int(input('Введите переменную b: '))

var_c = int(input('Введите переменную c: '))


print(my_func(var_a, var_b, var_c))
