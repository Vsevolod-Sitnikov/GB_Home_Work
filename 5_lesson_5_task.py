import random

sum_after_write = int()
sum_past_write = int()

list_number = [random.randint(-100, 100) for i in range(0, 10)]
print(list_number)


for i in list_number:
    sum_after_write += i


print(f'Сумма до записи составляет {sum_after_write}')


with open('file_5_task.txt', 'w') as file:
    for i in list_number:
        content = str(i) + ' '
        file.write(content)


with open('file_5_task.txt', 'r') as file:
    content = file.readline()


print(content)


for i in content.split():
    sum_past_write += int(i)


print(f'Сумма после записи составляет {sum_past_write}')
