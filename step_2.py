print('Время')
time = int(input("Введите время в секундах: "))
if time / 60 < 60:
    hh = 0
    if hh < 10:
        hh = str('0' + str(hh))
    else:
        hh = str(hh)
    mm = time // 60
    if mm < 10:
        mm = str('0' + str(mm))
    else:
        mm = str(mm)
    ss = time % 60
    if ss < 10:
        ss = str('0' + str(ss))
    else:
        ss = str(ss)
    print(f'''Время: {hh}:{mm}:{ss}''')
if time / 60 >= 60:
    hh = time // 3600
    if hh < 10:
        hh = str('0' + str(hh))
    else:
        hh = str(hh)
    mm = (time - 3600 * int(hh)) // 60
    if mm < 10:
        mm = str('0' + str(mm))
    else:
        mm = str(mm)
    ss = time - ((3600 * int(hh)) + (60 * int(mm)))
    if ss < 10:
        ss = str('0' + str(ss))
    else:
        ss = str(ss)
    print(f'''Время: {hh}:{mm}:{ss}''')
