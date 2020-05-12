from sys import argv
name, time, salary, bonus = argv
def zp():
    name, time, salary, bonus = argv
    res = int(time) * int(salary) + int(bonus)
    return res
print('Имя скрипта: ', name)
print('Выработка в часах: ', time)
print('Ставка в час: ', salary)
print('Премия: ', bonus)
print(f'Заработная плата сотрудника ', zp())

