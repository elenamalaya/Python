class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

inp_data = input('Введите знаменатель: ')
inp_data2 = input('Введите делитель: ')

try:
    inp_data = int(inp_data)
    inp_data2 = int(inp_data2)
    if inp_data == 0:
        raise OwnError('Делить на ноль нельзя!')
except ValueError:
    print('Введите числовое значение')
except OwnError as err:
    print(err)
else:
    print(f' Все хорошо Ваш результат {inp_data2/inp_data}')

