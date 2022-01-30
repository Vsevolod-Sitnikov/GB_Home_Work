#Вариант с костылем

numb_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

New_list = [elem for index, elem in enumerate(numb_list) if elem > numb_list[index-1]]

print(New_list[1:])
