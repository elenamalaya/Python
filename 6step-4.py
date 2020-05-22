class Car:
    # атрибуты
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # методы
    def go(self):
        return f'{self.name} машина поехала'

    def stop(self):
        return f'{self.name} машина остановилась'

    def turn_right(self):
        return f'{self.name} машина повернула направо'

    def turn_left(self):
        return f'{self.name} машина повернула налево'

    def show_speed(self):
        return f'Текущая скорость автомобиля {self.name} составляет {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость городского автомобиля {self.name} составляет {self.speed}')

        if self.speed > 40:
            return f'Городской автомобиль {self.name} превысил скорость'
        #else:
            #return f'Городской автомобиль {self.name} едет с нормальной скоростью'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость рабочего автомобиля {self.name} составляет {self.speed}')

        if self.speed > 60:
            return f'Рабочий автомобиль {self.name} превысил скорость'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} полицейская машина'
        else:
            return f'{self.name} не полицейкая машина'


Jaguar = SportCar(120, 'Red', 'Jaguar', False)
Hyundai = TownCar(55, 'White', 'Hyundai', False)
Autoexcavator = WorkCar(70, 'Orange', 'Autoexcavator', False)
Police = PoliceCar(110, 'Blue',  'Ford', True)
print(Autoexcavator.turn_left())
print(f'Когда {Hyundai.turn_right()}, тогда {Jaguar.stop()}')
print(f'Данные о рабочей машине - {Autoexcavator.go()}. {Autoexcavator.show_speed()}')
print(f'Цвет мащины {Autoexcavator.name} {Autoexcavator.color}')
print(f'{Jaguar.name} полицейская машина? {Jaguar.is_police}')
print(f'{Police.name}  полицейская машина? {Police.is_police}')
print(Jaguar.show_speed())
print(Hyundai.show_speed())
print(Police.police())
print(Police.show_speed())
