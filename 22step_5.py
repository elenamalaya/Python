rating = [7, 5, 3, 3, 2]
while True:
    r = input('Введите новое значение рейтинга: ')

    try:
        r = abs(int(r))
    except ValueError as e:
        print('Упс...Попробуйте еще разок')
        continue

    #r отсутствует в списке в списке
    if not rating.count(r):
        #вставляем впереди или вконце списка
        if r > rating[0]:
            rating.insert(0, r)
        elif r < rating[-1]:
            rating.append(r)
        # ищем куда вставить внутри списка
        else:
            for ind,f  in enumerate(rating):
                if r > f:
                    rating.insert(ind, r)
                    break
    #уже есть такое значение
    else:
        new_ind = rating.index(r) + rating.count(r)
        rating.insert(new_ind, r)

    print(rating)


