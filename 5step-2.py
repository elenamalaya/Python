"""
One - 1
Two - 2
Three - 3
Four - 4
"""
my_file = open('text_4.txt', 'r')
content = my_file.read()
print(f'Содержимое файла:\n {content}')
my_file = open('text_4.txt', 'r')
content = my_file.readlines()
print(f'Количество строк в файле - {len(content)}')
for i in range(len(content)):
    print(f'Количество символов {i + 1} - ой строки {len(content[i])}')
my_file = open('text_4.txt', 'r')
content = my_file.read()
content = content.split()
print(f'Общее количество слов - {len(content)}')
my_file.close()
