import time


class TrafficLight:
    _color = ['красный', 'желтый', 'зеленый']

    def running():
        main = True
        while main:
            # status = input('Введите статус светофора\n')
            # if status == 'False':
            #     break
            print(f'Светофор {TrafficLight._color[0]}')
            time.sleep(7)
            print(f'Светофор {TrafficLight._color[1]}')
            time.sleep(2)
            print(f'Светофор {TrafficLight._color[2]}')
            time.sleep(5)

traffic = TrafficLight.running()
