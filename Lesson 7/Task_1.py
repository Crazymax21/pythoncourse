# 1) Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод
# __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде
# прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
# 31 22
# 37 43
# 51 86
# 3 5 32
# 2 4 6
# -1 64 -8
# 3 5 8 3
# 8 3 7 1
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в
# привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух
# объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой
# строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

import numpy as np


class Matrix:
    _sub_matrix = []

    def __init__(self, user_matrix):
        self.sub_matrix = user_matrix

    def __str__(self):
        print(*self.sub_matrix, sep='\n')

    def validate_matrix(self, other):
        if len(self.sub_matrix) != len(other.sub_matrix):
            return False
        else:
            for i in range(len(self.sub_matrix)):
                if len(self.sub_matrix[i]) != len(other.sub_matrix[i]):
                    return False
        return True


    def __add__(self, other):
        if self.validate_matrix(other):
            return np.array(self.sub_matrix) + np.array(other.sub_matrix)
        else:
            return 'Сложить можно только матрицы одного размера'


user_list1 = [[1, 2], [3, 4]]
user_list2 = [[5, 6], [7, 8]]

user_matrix1 = Matrix(user_list1)
user_matrix2 = Matrix(user_list2)

user_matrix1.__str__()
user_matrix2.__str__()

user_matrix1.__add__(user_matrix2)

print(user_matrix1.__add__(user_matrix2))
