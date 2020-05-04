pp = input("Введите поисковый запрос: ")
p = pp.split()
for ind, el in enumerate(p):
   print(ind, el[:10])
