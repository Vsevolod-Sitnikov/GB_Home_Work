class Road:

    def __init__(self, lenght, width):
        self._lenght = int(lenght)
        self._width = int(width)

    def weight(self, thickness=1):
        return self._lenght * self._width * 25 * thickness


road = Road(lenght=200, width=50)
print(road.weight(thickness=5))
