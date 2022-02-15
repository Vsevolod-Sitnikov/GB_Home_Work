class NoDigit(Exception):

    def __init__(self, text):
        self.text = text

data_list = []

cicle = True

while cicle:
    data_input = input('введите число для добавления в список: ')
    if data_input == 'stop':
        cicle = False
    try:
        if data_input.isdigit() == True or data_input[0] == '-' and data_input[1:].isdigit() == True:
            data_list.append(int(data_input))
        else:
            raise NoDigit(f'Необходимо ввести число')
    except NoDigit as err:
        print(err)

print(f'Конечный список {data_list}')
