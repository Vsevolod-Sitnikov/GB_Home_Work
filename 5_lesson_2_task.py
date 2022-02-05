with open('file_2_task.txt', 'r', encoding='UTF-8') as file:
    content = file.readlines()

print(f'количество строк равно {len(content)}')

for index, string in enumerate(content, 1):
    print(f'В строке {index} количество слов равно  {len(string.split())}')
