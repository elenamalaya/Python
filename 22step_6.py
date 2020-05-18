tovary = []
characteristic = {'Название': '', 'Цена': '', 'Количество': '', 'Единица измерения': ''}
analytics = {'Название': [], 'Цена': [], 'Количество': [], 'Единица измерения': []}
i = 0
character = None
process = None
while True:
    process = input("Для окончания нажмите 'V', для продолжения нажмите 'Enter', для запроса аналитики нажмите 'A'").upper()
    if process == 'V':
        break
    i += 1
    if process == 'A':
        print('Аналитика о товарах')
        for key, value in analytics.items():
            print(f'{key[:15]:>20}: {value}')
    for j in characteristic.keys():
        character = input(f'Введите заначение параметра "{j}"')
        characteristic[j] = int(character) if (j == 'Цена' or j == 'Количество') else character
        analytics[j].append(characteristic[j])
    tovary.append((i, characteristic))
