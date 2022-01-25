new_string = input("Введите новую строку\n").split()

for index, element in enumerate(new_string, 1):
    print(index, element[:10])
