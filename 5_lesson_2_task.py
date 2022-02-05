with open('file_2_task.txt', 'r') as file:
    content = file.readlines()

print(f'количество строк равно {len(content)}')

for index, string in enumerate(content, 1):
    print(f'В строке {index} количество слов равно  {len(string.split())}')
