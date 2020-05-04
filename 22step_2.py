l = input("Введите список без разделителей: ")
l = list(l)
j = 0
for i in range(int(len(l) / 2)):
    l[j], l[j + 1] = l[j + 1], l[j]
    j += 2

print(l)
