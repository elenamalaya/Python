class OwnErrorNull:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"Делить на ноль нельзя!")


div = OwnErrorNull(2, 10)
print(OwnErrorNull.divide(10, 0))
print(OwnErrorNull.divide(10, 2))
print(div.divide(5, 0))

