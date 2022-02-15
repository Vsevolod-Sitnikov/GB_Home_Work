class Data:

    def __init__(self, data):
        self.data = data

    def __str__(self):
        return f'<Класс Дата>'

    @classmethod
    def data_to_int(cls, data):
        data_list = data.split('-')
        day = int(data_list[0])
        month = int(data_list[1])
        year = int(data_list[2])
        return day, month, year

    @staticmethod
    def valid_data(data):
        month_valid = {
            '01': 31, 
            '02': 28, 
            '03': 31, 
            '04': 30, 
            '05': 31, 
            '06': 30, 
            '07': 30, 
            '08': 31, 
            '09': 30, 
            '10': 31, 
            '11': 30, 
            '12': 31
        }
        data_list = data.split('-')
        for elem in data_list:
            if elem.isdigit() == False:
                return print(f"Элемент {elem} не является числом")
        if int(data_list[0]) > int(month_valid[data_list[1]]) and int(data_list[0]) < 0:
            return print(f"Некорректная дата. В месяце {month_valid[data_list[1]]} количество дней составляет  {month_valid[data_list[1]].value()}")
        else:
            return print('Дата корректна')

my_date = Data('05-02-2021')

print(my_date)

print(Data.data_to_int('05-02-2021'))

Data.valid_data('10-05-2021')
