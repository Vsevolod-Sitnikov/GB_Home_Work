import time


class TrafficLight:

    __colors = ['красный', 'желтый', 'зеленый']
    __timing = [7, 2, 5]

    def __init__(self):
        self.color = 'зеленый'

    def running(self):
        while True:
            for index, elem in enumerate(TrafficLight.__colors):
                print(f'Светофор {elem}')
                time.sleep(TrafficLight.__timing[index])


traffic = TrafficLight()

traffic.running()
