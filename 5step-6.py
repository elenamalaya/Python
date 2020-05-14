"""
Содержание исходного файла:
Fizra 0 30 0
Math 10 50 0
History 50 0 0
Physics 70 20 18
Informatics 40 12 20
Literature 10 0 8
Russian 0 0 90
"""

#import json

sub = {}
with open('text_66.txt', 'r') as file_sub:
    for line in file_sub:
        subject, lecture, practice, lab = line.split()
        sub[subject] = int(lecture) + int(practice) + int(lab)
    print(f'Общее количество часов по предмету: \n {sub}')