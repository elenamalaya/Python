import json
list_profit = {}
profit = {}
prof = 0
prof_average = 0
i = 0
with open('text_7.txt', 'r') as file:
    for line in file:
        name, form, rev, cost = line.split()
        list_profit[name] = int(rev) - int(cost)
        if list_profit.setdefault(name) >= 0:
            prof = prof + list_profit.setdefault(name)
            i += 1
    if i != 0:
        prof_average = prof / i
        print(f'Средняя прибыль - {prof_average:.2f}')
    else:
        print(f'Все фирмы убыточны.')
    profit = {'Average profit': round(prof_average)}
    # добавим в конец значение средней прибыли
    list_profit.update(profit)
    print(f'Прибыль каждой компании - {list_profit}')
# Создадим файл с расширением json
with open('text_7.json', 'w') as text_7_js:
    json.dump(list_profit, text_7_js)

    js_str = json.dumps(list_profit)
    print(f'Содержание файла с расширением json: \n '
          f' {js_str}')