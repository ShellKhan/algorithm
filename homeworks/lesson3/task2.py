# Задание 5.
# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

SIZE = 25
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]


def max_negative(mylist: list) -> tuple:
    """
    Функция принимает список и возвращает наибольшее из отрицательных значений списка и его индекс в списке
    """
    mnkey = 0
    mnval = float('-inf')
    for key, val in enumerate(mylist):
        if 0 > val > mnval:
            mnval = val
            mnkey = key
    return mnval, mnkey


print(array)
print(max_negative(array))
