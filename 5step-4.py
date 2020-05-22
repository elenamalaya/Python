"""
Данные в файле:
One - 1
Two - 2
Three - 3
Four - 4
"""

rus_dict = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []
with open('text_4.txt', 'r') as file_num:
    for i in file_num:
        i = i.split(' ', 1)
        new_file.append(rus_dict[i[0]] + '  ' + i[1])
    print(new_file)

# Запишем в новый файл результат:
with open('text_4_new.txt', 'w') as file_num_2:
    file_num_2.writelines(new_file)

# Проверка записи в новом файле:
my_f = open('text_4_new.txt', 'r')
content = my_f.readlines()
print(content)
my_f.close()