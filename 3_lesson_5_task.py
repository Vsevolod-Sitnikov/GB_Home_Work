def sum_func(number):
    """
    Функция рассчитывает сумму введенных цифр 
    :param number: вводимое число 
    :return: 
    """
    global end_sum
    end_sum = end_sum + number


end_sum = int()

end_flag = True

while end_flag:
    list_number = input('Введите список чисел. Разделителем является пробел. Для остановки введите #\n')
    for elem in list_number.split(' '):
        if elem == '#':
            end_flag = False
            break
        sum_func(int(elem))
    print(f'На данный момент сумма равна {end_sum}')

print(f'Конечная сумма равна {end_sum}')
