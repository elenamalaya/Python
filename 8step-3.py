class ErrorStr:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                num = int(input('Введите числовое значения и нажимайте Enter - '))
                self.my_list.append(num)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f"Вы ввели не число!")
                contin = input(f'Попробовать еще раз? Y/N ')

                if contin == 'Y' or contin == 'y':
                    print(try_except.my_input())
                elif contin == 'N' or contin == 'n':
                    print(f'Итоговый список - {self.my_list} \n ')
                    return f'Вы вышли'
                else:
                    print(f'Итоговый список - {self.my_list} \n ')
                    return f'Вы вышли'

try_except = ErrorStr(1)
print(try_except.my_input())