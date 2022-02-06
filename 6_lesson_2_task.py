class Road:

    def __init__(self, lenght, width):
        self.__lenght = int(lenght)
        self.__width = int(width)

    def weight(self, thickness=1):
        return self.__lenght * self.__width * 25 * thickness


road = Road(lenght=200, width=50)
print(road.weight(thickness=5))
