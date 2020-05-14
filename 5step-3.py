"""
Данные в файле такие:
Ivanov 10000.0
Petrov 15000.0
Sidorov 25000.1
Ivanova 15000.7
Petrova 19000.9
Sidorova 26000.1
Octouber 30000.5
Petrouber 26000.4
Znamenskiy 12000.0
Koreckiy 31000.9
"""
with open('text_3.txt', 'r') as my_file:
    zp = []
    zp_min = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if float(i[1]) < 20000:
           zp_min.append(i[0])
        zp.append(i[1])
print(f'Оклад меньше 20.000 {zp_min}, средний оклад {sum(map(float, zp)) / len(zp)}')