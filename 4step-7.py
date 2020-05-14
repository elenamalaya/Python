from itertools import count
from math import factorial

def fact():
    for el in count(1):
        yield factorial(el)

gen = fact()
i = 0
for n in gen:
    if i < 5:
        print(n)
        i += 1
    else:
        break

