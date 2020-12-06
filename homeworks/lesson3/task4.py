# Задание 3.
# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 25
MIN_ITEM = 0
MAX_ITEM = 25
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]


def max_n_min(mylist: list) -> tuple:
    """
    Функция принимает список и возвращает наименьшее и наибольшее значения и их индексы
    """
    max_ = float('-inf')
    min_ = float('inf')
    keymax = 0
    keymin = 0
    for key, value in enumerate(mylist):
        if value > max_:
            max_ = value
            keymax = key
        elif value < min_:
            min_ = value
            keymin = key
    return keymax, max_, keymin, min_


print(array)
key1, val1, key2, val2 = max_n_min(array)
array[key1], array[key2] = val2, val1
print(array)
