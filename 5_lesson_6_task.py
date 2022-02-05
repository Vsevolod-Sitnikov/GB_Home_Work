import re

dictionary_disciplines = {}

with open('file_6_task.txt', encoding='UTF-8') as file:
    for line in file:
        sum_time_disciplines = int()
        line_list = line.split(':')
        first_line_list = line.split(' ')
        for i in first_line_list:
            result = re.search(r'[-+]?\d+', i)
            if result != None:
                sum_time_disciplines += int(result[0])
        dictionary_disciplines[line_list[0]] = sum_time_disciplines

print(dictionary_disciplines)
