class Type_Devices_Exception(Exception):

    def __init__(self, text):
        self.text = text


class Sklad:

    def __init__(self):
        self.devices_on_the_sklad = {}

    def add_devices(self, devices):
        for device in devices:
            serial_number = device.get_serial_number()
            if self.devices_on_the_sklad.get(serial_number):
                self.devices_on_the_sklad[serial_number] += 1
            else:
                self.devices_on_the_sklad[serial_number] = 1

    def remove_device(self, device):
        device_serial_number = device.get_serial_number()
        if self.devices_on_the_sklad.get(device_serial_number):
            self.devices_on_the_sklad[device_serial_number] -= 1
            if self.devices_on_the_sklad[device_serial_number] == 0:
                self.devices_on_the_sklad.pop([device_serial_number])
            return True
        return False


    def show_inventory(self):
        return self.devices_on_the_sklad

    def show_all_cost(self):
        all_cost = int()
        for key, value in devices_on_the_sklad:
            all_cost += Orgtekhnika.get_cost_device()


class Orgtekhnika:

    __serial_number = 1

    def __init__(self, color, cost):
        self.color = color
        self.cost = cost
        self.serial_number = Orgtekhnika.__serial_number
        Orgtekhnika.__serial_number += 1

    def get_serial_number(self):
        return self.serial_number

    def get_cost_device(self):
        return self.cost


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
