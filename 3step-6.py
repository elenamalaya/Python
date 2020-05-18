"""
Функция, которая меняет в слове первую букву на прописную,
остальные оставляя как есть:
"""
def int_func(word):
    first_letter_small = word[0]
    first_letter_big = chr(ord(first_letter_small) - ord('a') + ord('A'))
    return first_letter_big + word[1:]

"""
Сама процедура:
"""
words = input('Введите слова из латинских букв: ').split()
line = []
for word in words:
    line.append(int_func(word))
print(' '.join(line))