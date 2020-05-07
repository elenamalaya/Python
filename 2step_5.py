print("Рейтинг невозрастающего набора чисел")
my_list = [7, 5, 3, 3, 2]
r = int(input("Введите новый элемент Рейтинга: "))
my_tsil = my_list[::-1]
print(my_tsil)
j = 0
while my_tsil[j] != my_tsil[j + 1]:

    if r > max(my_list):
        my_list.insert(0, r)
        print(my_list)
    if r < min(my_list):
        my_tsil.insert(0, r)
        print(my_tsil[::-1])
#эта часть почему то не работает
        my_tsil.insert(j - 2, r)
        print(my_tsil[::-1])
        j = j + 1


