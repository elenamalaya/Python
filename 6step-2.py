class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass1(self):
        return self._length * self._width


class MassCount(Road):
    def __init__(self, _length, _width, m, h):
        super().__init__(_length, _width)
        self.m = m
        self.h = h


r = MassCount(20, 5000, 25, 5)
print("Масса асфальта", r.mass1()*r.m * r.h/1000, "тонн")

