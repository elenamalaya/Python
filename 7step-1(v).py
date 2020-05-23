class Matrix:

    def __init__(self, list):
        self.list = list

    def __str__(self):
        return '\n'.join('\t'.join([str(i) for i in j]) for j in self.list)

    def __add__(self, other):
        try:
            matr = [[int(self.list[j][i]) + int(other.list[j][i]) for i in range(len(self.list[j]))]
                 for j in range(len(self.list))]
            return Matrix(matr)
        except IndexError:
            return f'Ошибка суммы из-за разности размерностей матриц'


m_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m_2 = [[2, 3, 4], [5, 6, 7], [8, 9, 10]]

matr_1 = Matrix(m_1)
matr_2 = Matrix(m_2)
new_matr = matr_1 + matr_2

print(matr_1,'\n')
print(matr_2,'\n')
print(matr_1+matr_2)