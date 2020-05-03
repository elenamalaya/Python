while True:
    try:
        my_list = [ [12, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11] ]
        m = int(input("Введите номер месяца от 1 до 12: "))
        if m in my_list[0]:
            print("Месяц относится к Зиме")
        if m in my_list[1]:
            print("Месяц относится к Весне")
        if m in my_list[2]:
            print("Месяц относится к Лету")
        if m in my_list[3]:
            print("Месяц относится к Осени")
        else:
            print('Введенное значение не корректно, пожалуйста, попробуйте еще разок')
        break
    except ValueError:
        print("Пожалуйста введите числовое значение")