from itertools import count
list = []
for el in count(3):
    if el > 5:
        break
    else:
        list.append(int(el))
        print(list)
"""
Применение функции repeat вместо break:
"""
from itertools import cycle,repeat
c=0
for el in repeat(list,5):
    # if c > 10:
        # break
    print(el)
    c = c+1
