my_list = input('Введите текст для списка. разделителем является пробел\n').split(' ')

counter = 1

while counter < len(my_list):
    my_list[counter], my_list[counter-1] = my_list[counter-1], my_list[counter]
    counter += 2

print(my_list)
