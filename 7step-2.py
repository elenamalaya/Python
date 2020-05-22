class Сlothes:
    def __init__(self, v, h):
        self.v = v
        self.h = h

    def material_c(self):
        return round(self.v / 6.5 + 0.5)

    def material_s(self):
        return round(self.h * 2 + 0.3)

    @property
    def material_full(self):
        return str(f'Общий расход ткани \n'
                   f'{round((self.v / 6.5 + 0.5) + (self.h * 2 + 0.3))}')


class Coat(Сlothes):
    def __init__(self, v, h):
        super().__init__(v, h)
        self.cons_c = round(self.v / 6.5 + 0.5)

    def __str__(self):
        return f'Расход ткани на пальто {self.cons_c}'


class Suit(Сlothes):
    def __init__(self, v, h):
        super().__init__(v, h)
        self.cons_j = round(self.h * 2 + 0.3)

    def __str__(self):
        return f'Расход ткани на костюм {self.cons_j}'

coat = Coat(5, 10)
suit = Suit(12, 5)
print(coat)
print(suit)
print(coat.material_full)
print(suit.material_full)
print(suit.material_c())
print(suit.material_s())