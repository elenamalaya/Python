from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    @property
    def consumption(self):
        return f"Расход ткани на пальто - {round(self.param / 6.5) + 0.5}"

class Costume(Clothes):
    @property
    def consumption(self):
        return f"Расход ткани на костюм - {2 * self.param + 0.3}"

class Total(Clothes):
    @property
    def consumption(self):
        return f"Общий расход ткани - {(2 * self.param + 0.3) + (round(self.param / 6.5) + 0.5)}"

coat = Coat(60)
costume = Costume(60)
total = Total(60)
print(coat.consumption)
print(costume.consumption)
print(total.consumption)
