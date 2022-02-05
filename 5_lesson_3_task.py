# первый вариант решения - более долгая обработка данных
content = {}

average = 0

counter = 0

with open('file_3_task.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        line_split = line.split(' ')
        content[line_split[0]] = float(line_split[1][:-1])


for key, value in content.items():
    if value < float(20000):
        print(f'{key} имеет доход менее 20000. Доход составляет {value}')
    average += value
    counter += 1
print(f'Средний доход составляет {round(average / counter, 2)}')

# более лаконичный вариант решения
average = 0
counter = 0

with open('file_3_task.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        line_split = line.split(' ')
        if float(line_split[1][:-1]) < 20000:
            print(f'{line_split[0]} имеет доход менее 20000. Доход составляет {line_split[1][:-1]}')
        average += float(line_split[1][:-1])
        counter += 1

print(f'Средний доход составляет {round(average / counter, 2)}')
