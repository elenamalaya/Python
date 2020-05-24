print('Проект "Склад оргтехники"')
class OfficeEquipment:

    def __init__(self, name, price, quantity, numb, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = numb
        self.my_store_full = []
        self.my_store = []
        self.my_list = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'

    def warehouse(self):

        try:
            unit = input(f'Введите наименование товара ')
            unit_p = int(input(f'Введите цену за ед. '))
            unit_q = int(input(f'Введите количество '))
            unique = {'Модель устройства': unit, 'Цена за ед': unit_p, 'Количество': unit_q}
            self.my_list.update(unique)
            self.my_store.append(self.my_list)
            print(f'Текущий список товаров -\n {self.my_store}')
        except:
            return f'Ошибка ввода данных'

        print(f'Для выхода - Q, продолжение - Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Весь склад -\n {self.my_store_full}')
            return f'Выход'
        else:
            return OfficeEquipment.warehouse(self)


class Printer(OfficeEquipment):
    def printt(self):
        return f'Напечатать {self.numb} раз'


class Scanner(OfficeEquipment):
    def scann(self):
        return f'Сканировать {self.numb} раз'


class Copier(OfficeEquipment):
    def copierr(self):
        return f'Копировать  {self.numb} раз'


unit_1 = Printer('hp', 4500, 2, 4)
unit_2 = Scanner('Canon', 3000, 3, 10)
unit_3 = Copier('Xerox', 5000, 1, 5)
print(unit_1.warehouse())
#print(unit_2.warehouse())
#print(unit_3.warehouse())
print('\n', unit_1.printt())
print(unit_2.scann())
print(unit_3.copierr())