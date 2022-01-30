my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

new_list = [elem for index, elem in enumerate(my_list) if elem not in my_list[:index] and elem not in my_list[index+1:]]

print(new_list)
