class Data:

    def __init__(self, data):
        self.data = data

    def __str__(self):
        return f'<Класс Дата>'

    def __doc__(self):
        """
        Класс даты. Для создания объекта необходимо ввести дату в формате «день-месяц-год»
        :return:
        """

    @classmethod
    def data_to_int(cls, data):
        data_list = data.split('-')
        day = int(data_list[0])
        month = int(data_list[1])
        year = int(data_list[2])
        return day, month, year

    @staticmethod
    def valid_data():
        pass

my_date = Data('05-02-2021')

print(my_date)

print(Data.data_to_int('05-02-2021'))
