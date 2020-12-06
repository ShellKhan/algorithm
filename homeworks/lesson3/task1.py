# Задание 7.
# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

SIZE = 25
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]


def two_less(mylist: list) -> tuple:
    """
    Функция принимает список и возвращает наименьшее и второе по величине значения списка
    """
    minimal = float('inf')
    subminimal = float('inf')
    for i in mylist:
        if i < minimal:
            subminimal = minimal
            minimal = i
        elif i < subminimal:
            subminimal = i
    return minimal, subminimal


print(array)
print(two_less(array))
