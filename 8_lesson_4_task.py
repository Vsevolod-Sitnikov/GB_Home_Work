from abc import ABC, abstractmethod


class Type_Devices_Exception(Exception):

    def __init__(self, text):
        self.text = text


class SkladInterfaces(ABC):
    '''
    Интерфейс класса Склад
    Методы:
    add_devices - добавить устройство или устройства
    remove_device - удалить устройство
    show_inventory - посмотреть какие устройства есть на складе
    :return:
    '''

    @abstractmethod
    def add_devices(self):
        pass

    @abstractmethod
    def remove_device(self):
        pass

    @abstractmethod
    def show_inventory(self):
        pass


class Sklad(SkladInterfaces):

    __all_cost_devices = int()

    def __init__(self):
        self.devices_on_the_sklad = {}

    def add_devices(self, devices):
        for device in devices:
            serial_number = device.get_serial_number()
            if self.devices_on_the_sklad.get(serial_number):
                self.devices_on_the_sklad[serial_number] += 1
            else:
                self.devices_on_the_sklad[serial_number] = 1
            Sklad.__all_cost_devices += device.cost

    def remove_device(self, device):
        device_serial_number = device.get_serial_number()
        if self.devices_on_the_sklad.get(device_serial_number):
            self.devices_on_the_sklad[device_serial_number] -= 1
            if self.devices_on_the_sklad[device_serial_number] == 0:
                self.devices_on_the_sklad.pop(device_serial_number)
            Sklad.__all_cost_devices -= device.cost
            return True
        return False

    def show_inventory(self):
        return self.devices_on_the_sklad

    @classmethod
    def show_all_cost(cls):
        return cls.__all_cost_devices


class Departament:
    pass



class Orgtekhnika:

    __serial_number = 1

    def __init__(self, color, cost):
        self.color = color
        try:
            self.cost = cost
            if type(cost) != int:
                raise Type_Devices_Exception(f'Необходимо ввести значение в численом формате')
        except Type_Devices_Exception as err:
            print(err)
        self.serial_number = Orgtekhnika.__serial_number
        Orgtekhnika.__serial_number += 1

    def get_serial_number(self):
        return self.serial_number

    def get_cost_device(self):
        return self.cost

    @classmethod
    def count_used_serial_number(cls):
        return cls.__serial_number


class Printer(Orgtekhnika):
    def __init__(self, color, cost, model):
        Orgtekhnika.__init__(self, color, cost)
        self.model = model

    def parameters(self):
        return f'Тип принтер. Модель {self.model}. Цвет {self.color}. Стоимость {self.cost}'


class Skaner(Orgtekhnika):
    def __init__(self, color, cost, model):
        Orgtekhnika.__init__(self, color, cost)
        self.model = model

    def parameters(self):
        return f'Тип сканер. Модель {self.model}. Цвет {self.color}. Стоимость {self.cost}'



class Xerox(Orgtekhnika):
    def __init__(self, color, cost, model):
        Orgtekhnika.__init__(self, color, cost)
        self.model = model

    def parameters(self):
        return f'Тип ксерокс. Модель {self.model}. Цвет {self.color}. Стоимость {self.cost}'


my_printer = Printer('black', 22500, 'HP 2205Z')

print(my_printer.get_serial_number())

print(my_printer.parameters())

new_xerox = Xerox('white', 5000, 'YZ500R')

new_sklad = Sklad()

new_sklad.add_devices([new_xerox, my_printer])

print(new_xerox.parameters())

print(new_sklad.show_inventory())

print(new_sklad.show_all_cost())

new_sklad.remove_device(new_xerox)

print(new_sklad.show_all_cost())

print(new_sklad.show_inventory())

new_printer_for_err = Printer('black', '123', 'HP 2205Z')

print(SkladInterfaces.__doc__)
