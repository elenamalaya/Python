from time import sleep


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        i = 0
        while i < 3:
            print(f'Светофор переключается \n '
                  f'{TrafficLight.__color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(7)
            i += 1

    def out_red(text):
        print("\033[31m {}" .format(text))

    def out_yellow(text):
        print("\033[33m {}".format(text))

    def out_green(text):
        print("\033[32m {}" .format(text))



TrafficLight = TrafficLight()
TrafficLight.running()