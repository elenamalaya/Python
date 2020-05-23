print('Вывод результата деления: ')


def my_div():
    try:
        arg1 = int(input("Введите делимое: "))
        arg2 = int(input("Введите делитель: "))
        result_div = arg1 / arg2

    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "Ошибка! Делить на ноль нельзя!"

    return result_div


print(my_div())
