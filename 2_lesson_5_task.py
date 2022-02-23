my_list = [9, 7, 5, 4, 3, 2]

len_list = len(my_list)

input_new_number = int(input('Введите число\n'))

for index, element in enumerate(my_list):
    if input_new_number > element:
        my_list.insert(index, input_new_number)
        break

if len_list == len(my_list):
    my_list.append(input_new_number)

print(my_list)
