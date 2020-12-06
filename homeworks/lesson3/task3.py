# Задание 9.
# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

SIZE_H = 5
SIZE_V = 5
MIN_ITEM = -100
MAX_ITEM = 100
matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_H)] for _ in range(SIZE_V)]


def minbar(mymatrix: list, barnum: int) -> int:
    """
    Функция принимает матрицу и номер столбца и возвращает минимум этого столбца
    """
    ret = float('inf')
    for line in mymatrix:
        if line[barnum] < ret:
            ret = line[barnum]
    return ret


def minimax(mymatrix: list) -> int:
    """
    Функция принимает матрицу и возвращает наибольший среди минимумов столбцов
    """
    ret = float('-inf')
    for point, value in enumerate(mymatrix[0]):
        if minbar(mymatrix, point) > ret:
            ret = minbar(mymatrix, point)
    return ret


print(matrix)
print(minimax(matrix))
