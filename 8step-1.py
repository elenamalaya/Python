class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def number(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 1 <= year <= 2020:
                    return f'Дата введена верно'
                else:
                    return f'Такого года еще не было'
            else:
                return f'Такого месяца не существует'
        else:
            return f'Такого дня не существует'

    def __str__(self):
        return f'Текущая дата {Data.number(self.day_month_year)}'


today = Data('24 - 5 - 2020')
print(today)
print(Data.valid(24, 5, 2030))
print(today.valid(24, 15, 2020))
print('Просто число: ', Data.number('25 - 5 - 2020'))
print('Сегодня: ',today.number('24 - 5 - 2020'))
print(Data.valid(10, 10, 1000))