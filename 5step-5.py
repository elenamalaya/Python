def summa():
    try:
        with open('summa.txt', 'w+') as my_sum:
            line = input('Введите цифры через пробел \n')
            my_sum.writelines(line)
            my_num = line.split()

            print(sum(map(int, my_num)))
    except IOError:
        print('Ошибка')
    except ValueError:
        print('Упс... что то пошло не так. Пожалуйста попробуйте еще:')
    except NameError:
        print('Упс... что то пошло не так. Пожалуйста попробуйте еще:')

summa()