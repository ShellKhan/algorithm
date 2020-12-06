# Задание 6.
# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]


def max_n_min(mylist: list) -> tuple:
    """
    Функция принимает список и возвращает индексы наименьшего и наибольшего значений
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
    return keymax, keymin


key_b, key_e = max_n_min(array)
if key_b > key_e:
    key_b, key_e = key_e, key_b
sum_ = 0
for key, value in enumerate(array):
    if key_b < key < key_e:
        sum_ += value
print(array)
print(sum_)
