class Stationery:
    # атрибуты
    def __init__(self, title):
        self.title = title

    # методы
    def draw(self):
        return f'{self.title} Запуск отрисовки'


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Запуск отрисовки {self.title} ручкой'


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Запуск отрисовки {self.title} карандашем'


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Запуск отрисовки {self.title} маркером'


step1 = Pen('Портрета')
step2 = Pencil('Чертежа')
step3 = Handle('Плана')
print(step1.draw())
print(step2.draw())
print(step3.draw())
