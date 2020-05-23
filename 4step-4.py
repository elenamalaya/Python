from random import randint
my_list = []
i = 1
m = int(input('сколько элементом нужно в спике:'))
while i <= m:
    my_list.append(randint(1,20))
    i += 1
print(my_list)

# my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
my_new_list = [el for el in my_list if my_list.count(el) < 2]
print(my_new_list)