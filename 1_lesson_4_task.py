number = input("Введит целое положительное число\n")

counter = int(0)

end_result = int(0)

while counter < len(number):
    if int(number[counter]) > end_result:
        end_result = int(number[counter])
    counter += 1

print(f"Максимальная цифра из числа равна {end_result}")
