class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        Worker.__init__(self, name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'{self.name}, {self.surname} (должность {self.position})'

    def get_total_income(self):
        return f'Общий доход составляет {self._income["wage"] + self._income["bonus"]}'


engineer = Position('antoan', 'antonov', 'engineer', 500, 1300)

print(engineer.get_full_name())
print(engineer.get_total_income())
