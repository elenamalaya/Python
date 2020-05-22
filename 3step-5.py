def my_sum ():
    sum_i = 0
    proces = False
    while proces == False:
        number = input('Для подсчета суммы ведите числа разделеные пробелом или Q для завершения - ').split()

        i = 0
        for j in range(len(number)):
            if number[j] == 'q' or number[j] == 'Q':
                proces = True
                break
            else:
                i = i + int(number[j])
        sum_i = sum_i + i
        print(f'Промежуточная сумма равна: {sum_i}')
    print(f'Финальная сумма равна: {sum_i}')


my_sum()
