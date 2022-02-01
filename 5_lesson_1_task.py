close_flag = True


with open('file_1_task.txt', 'w') as file:
    while close_flag:
        write_line = input('введите необходимую запись:\n')
        if write_line == '':
            close_flag = False
        file.writelines(write_line + '\n')


print('Запись в файл произведена')
