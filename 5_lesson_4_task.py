dictionary = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

new_string_list = []

with open('file_4_task.txt', encoding='UTF-8') as file:
    for line in file:
        line_content = line.split(' ')
        new_string = line_content[0] + ' ' + line_content[1] + ' ' + line_content[2]
        new_string_list.append(new_string)

print(new_string_list)
with open('file_4_task_write.txt', 'w') as file_2:
    for elem in new_string_list:
        file_2.write(elem)
