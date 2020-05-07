print('Ежедневные пробежки спортсмена')
a = int(input("Количество км в первый день: "))
b = int(input("Необходимое количесвто км в день: "))
day = 1
while b > a:
    a = 0.1*a+a
    day = day + 1
    continue
print(day)