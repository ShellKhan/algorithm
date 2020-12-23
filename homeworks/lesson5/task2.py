# Задание 2.
# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
# коллекция, элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и
# [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque

ORDER = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']


def hex_prn(a: deque) -> str:
    """
    преобразование очереди в строку для красивого вывода
    :param a: очередь
    :return: строка
    """
    res = ''
    for i in range(len(a)):
        res += a[i]
    return res


def hex_add(d: deque, c: deque) -> deque:
    """
    сложение в столбик
    :param d: первое слагаемое
    :param c: второе слагаемое
    :return: результат
    """
    a = d.copy()
    b = c.copy()
    a.reverse()
    b.reverse()
    if len(a) < len(b):
        a, b = b, a
    if len(a) != len(b):
        for _ in range(len(a) - len(b)):
            b.append('0')
    res = deque([])
    trans = 0
    for i in range(len(a)):
        spam = ORDER.index(a[i]) + ORDER.index(b[i]) + trans
        trans = spam // 16
        res.appendleft(ORDER[spam % 16])
    if trans:
        res.appendleft(ORDER[trans])
    return res


def hex_mul_one(d: deque, b: str) -> deque:
    """
    вспомогательная операция умножения числа на одну цифру для умножения в столбик
    :param d: число
    :param b: цифра
    :return: результат
    """
    a = d.copy()
    res = deque([])
    trans = 0
    a.reverse()
    for i in a:
        spam = (ORDER.index(i) * ORDER.index(b)) + trans
        trans = spam // 16
        res.appendleft(ORDER[spam % 16])
    if trans:
        res.appendleft(ORDER[trans])
    return res


def hex_mul(d: deque, c: deque) -> deque:
    """
    умножение в столбик
    :param d: первый множитель
    :param c: второй множитель
    :return: результат
    """
    a = d.copy()
    b = c.copy()
    res = deque([])
    array = []
    add_zero = 0
    b.reverse()
    for i in b:
        spam = hex_mul_one(a, i)
        for _ in range(add_zero):
            spam.append('0')
        array.append(spam)
        add_zero += 1
    for j in range(len(array)):
        res = hex_add(res, array[j])
    return res


prime = deque(input("Введите первое число: ").upper())
second = deque(input("Введите второе число: ").upper())
print(f'Сумма - {hex_prn(hex_add(prime, second))}')
print(f'Произведение - {hex_prn(hex_mul(prime, second))}')
