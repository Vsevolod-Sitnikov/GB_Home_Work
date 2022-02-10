class Road:

    def __init__(self, lenght, width):
        self._lenght = int(lenght)
        self._width = int(width)

    def weight(self, asphalt_mass=25, thickness=1):
        return self._lenght * self._width * asphalt_mass * thickness / 1000


road = Road(lenght=200, width=50)
print(road.weight(thickness=5))
