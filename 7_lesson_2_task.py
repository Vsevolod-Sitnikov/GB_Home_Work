from abc import ABC, abstractmethod


class Shoes(ABC):
    @abstractmethod
    def amount_of_fabric(self):
        pass

class Coat(Shoes):

    def __init__(self, size):
        self.size = size

    @property
    def amount_of_fabric(self):
        result = self.size / 6.5 + 0.5
        return round(result, 3)

class costume(Shoes):

    def __init__(self, height):
        self.height = height

    @property
    def amount_of_fabric(self):
        result = 2 * self.height + 0.3
        return round(result, 3)


new_coat = Coat(48)

print(new_coat.amount_of_fabric)

new_costume = costume(180)

print(new_costume.amount_of_fabric)
