class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self._is_police = is_police

    def go(self):
        return 'машина двигается'

    def stop(self):
        return 'машина остановилась'

    def turn(self, direction):
        return f'машина повернула на {direction}'

    def show_speed(self):
        if self.speed >= 60:
            return f'Текущая скорость {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name, is_police=False)

    def show_speed(self):
        if self.speed >= 60:
            return f'Скорость слишком высокая ({self.speed})'


class WorkCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name, is_police=False)

    def show_speed(self):
        if self.speed >= 40:
            return f'Скорость слишком высокая ({self.speed})'


class SportCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name, is_police=False)


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name, is_police=True)


polo_car = Car(70, 'green', 'VW Polo', False)

jetta = TownCar(75, 'red', 'VW')

ferrari = SportCar(150, 'blue', 'Ferrari')

print(jetta.show_speed())

print(polo_car.show_speed())

print(ferrari.go())
print(ferrari.stop())
print(ferrari.turn('left'))
