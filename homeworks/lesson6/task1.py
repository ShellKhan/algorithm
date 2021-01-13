# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в задания 3.7.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Для исследования взята задача 3.7, как и в домашнем задании 4.
# Кроме измерения памяти подключена функция трассировки. Ни для чего, просто захотелось посмотреть, как она работает.
# Как оказалось, трассировочная функция без дополнительных ухищрений отрабатывает только на входе в функцию,
# поэтому мерить память при ее вызове нельзя.
# Дополнительно было проверено, изменяется ли размер переменной, используемой для обхода массива в цикле,
# сразу после окончания цикла. Оказалось, что не меняется. Что интересно, он может меняться в самом цикле,
# когда попадается элемент массива, равный 0. Команды этого замера закомментированы.

import random
import sys

# Константы запуска
SIZE = 1000
MIN_ITEM = -100
MAX_ITEM = 100
ARRAY = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

# Константы измерений
VERSION_STR = 'Версия системы: MSWindows ' + str(sys.getwindowsversion().major)
BIT_DEPTH_STR = 'Разрядность системы: ' + sys.platform
PYTHON_STR = 'версия пайтона: ' + sys.winver
ARRAY_WEIGHT = str(sys.getsizeof(ARRAY))


# Исследующий инструмент
def trace_func(frame, event, arg):
    print(f'FRAME: {str(frame)}, EVENT: {str(event)}, ARG: {str(arg)}.')


report = list()


# Исследуемые функции
# 1. Мое решение - через заведомо большие значения float(Inf)
def two_less_1(mylist: list) -> tuple:
    global report
    report.append('Function "two_less_1" begin')
    report.append('Memory taken:')
    size = sys.getsizeof(mylist)
    report.append(f'list - {size}')
    minimal = float('inf')
    subminimal = float('inf')
    spam = sys.getsizeof(minimal) + sys.getsizeof(subminimal)
    report.append(f'two minimals begin - {spam}')
    # print('CYCLE!', end=' ')
    for i in mylist:
        # print(str(sys.getsizeof(i)), end=' ')
        # if sys.getsizeof(i) != 28:
        #     print(f'({i})', end=' ')
        if i < minimal:
            subminimal = minimal
            minimal = i
        elif i < subminimal:
            subminimal = i
    # print('STOP!')
    report.append(f'cycle pointer - {sys.getsizeof(i)}')
    size += sys.getsizeof(i)
    size += spam if spam > (sys.getsizeof(minimal) + sys.getsizeof(subminimal)) else (
            sys.getsizeof(minimal) + sys.getsizeof(subminimal))
    report.append(f'two minimals end - {sys.getsizeof(minimal) + sys.getsizeof(subminimal)}')
    report.append(f'Function maximum memory size = {size}')
    return minimal, subminimal


# 2. Решение преподавателя - через первые два значения массива, в индексах
def two_less_2(mylist: list) -> tuple:
    global report
    report.append('Function "two_less_2" begin')
    report.append('Memory taken:')
    size = sys.getsizeof(mylist)
    report.append(f'list - {size}')
    minimal, subminimal = (0, 1) if mylist[0] < mylist[1] else (1, 0)
    spam = sys.getsizeof(minimal) + sys.getsizeof(subminimal)
    report.append(f'two minimals begin - {spam}')
    # print('CYCLE!', end=' ')
    for i in range(2, len(mylist)):
        # print(str(sys.getsizeof(i)), end=' ')
        # if sys.getsizeof(i) != 28:
        #     print(f'({i})', end=' ')
        if mylist[i] < mylist[minimal]:
            eggs = minimal
            minimal = i
            if mylist[eggs] < mylist[subminimal]:
                subminimal = eggs
        elif mylist[i] < mylist[subminimal]:
            subminimal = i
    # print('STOP!')
    report.append(f'cycle pointer - {sys.getsizeof(i)}')
    size += sys.getsizeof(i)
    size += spam if spam > (sys.getsizeof(minimal) + sys.getsizeof(subminimal)) else (
            sys.getsizeof(minimal) + sys.getsizeof(subminimal))
    report.append(f'two minimals end - {sys.getsizeof(minimal) + sys.getsizeof(subminimal)}')
    report.append(f'Function maximum memory size = {size}')
    return mylist[minimal], mylist[subminimal]


# 3. Решение преподавателя с заменой индексов на значения (устраняем влияние использования индексов)
def two_less_3(mylist: list) -> tuple:
    global report
    report.append('Function "two_less_3" begin')
    report.append('Memory taken:')
    size = sys.getsizeof(mylist)
    report.append(f'list - {size}')
    minimal, subminimal = (mylist[0], mylist[1]) if mylist[0] < mylist[1] else (mylist[1], mylist[0])
    spam = sys.getsizeof(minimal) + sys.getsizeof(subminimal)
    report.append(f'two minimals begin - {spam}')
    # print('CYCLE!', end=' ')
    for i in range(2, len(mylist)):
        # print(str(sys.getsizeof(i)), end=' ')
        # if sys.getsizeof(i) != 28:
        #     print(f'({i})', end=' ')
        if mylist[i] < minimal:
            eggs = minimal
            minimal = mylist[i]
            if eggs < subminimal:
                subminimal = eggs
        elif mylist[i] < subminimal:
            subminimal = mylist[i]
    # print('STOP!')
    report.append(f'cycle pointer - {sys.getsizeof(i)}')
    size += sys.getsizeof(i)
    size += spam if spam > (sys.getsizeof(minimal) + sys.getsizeof(subminimal)) else (
            sys.getsizeof(minimal) + sys.getsizeof(subminimal))
    report.append(f'two minimals end - {sys.getsizeof(minimal) + sys.getsizeof(subminimal)}')
    report.append(f'Function maximum memory size = {size}')
    return minimal, subminimal


# 4. Решение без присвоения начального значения (проверяем влияние дополнительного ветвления алгоритма)
def two_less_4(mylist: list) -> tuple:
    global report
    report.append('Function "two_less_4" begin')
    report.append('Memory taken:')
    size = sys.getsizeof(mylist)
    report.append(f'list - {size}')
    minimal = None
    subminimal = None
    spam = sys.getsizeof(minimal) + sys.getsizeof(subminimal)
    report.append(f'two minimals begin - {spam}')
    # print('CYCLE!', end=' ')
    for i in mylist:
        # print(str(sys.getsizeof(i)), end=' ')
        # if sys.getsizeof(i) != 28:
        #     print(f'({i})', end=' ')
        if not minimal:
            minimal = i
        elif not subminimal:
            if i > minimal:
                subminimal = i
            else:
                subminimal = minimal
                minimal = i
        elif i < minimal:
            eggs = minimal
            minimal = i
            if eggs < subminimal:
                subminimal = eggs
        elif i < subminimal:
            subminimal = i
    # print('STOP!')
    report.append(f'cycle pointer - {sys.getsizeof(i)}')
    size += sys.getsizeof(i)
    size += spam if spam > (sys.getsizeof(minimal) + sys.getsizeof(subminimal)) else (
            sys.getsizeof(minimal) + sys.getsizeof(subminimal))
    report.append(f'two minimals end - {sys.getsizeof(minimal) + sys.getsizeof(subminimal)}')
    report.append(f'Function maximum memory size = {size}')
    return minimal, subminimal


sys.settrace(trace_func)
report.append('Исходные данные:')
report.append(f'{VERSION_STR}. {BIT_DEPTH_STR}. {PYTHON_STR}.')
report.append(f'Размер памяти, занятый исходным списком: {ARRAY_WEIGHT}.')
two_less_1(ARRAY)
two_less_2(ARRAY)
two_less_3(ARRAY)
two_less_4(ARRAY)
print('\n'.join(report))

# В результате исследования оказалось, что ни один из вариантов алгоритма не дает преимущества по использованию памяти.
# Если в начале в первой функции используется меньше на 8 байт, а в четвертой даже на 24 байта,
# то в конце выполнения функций эта разница исчезает.
# Теоретически возможна еще флуктуация на 4 байта, если в последнем цикле указатель окажется равным нулю,
# но на практике мне такого увидеть не удалось.
#
# Пример выдачи в результате исполнения файла:
#
# "C:\Program Files\Python38\python.exe" C:/Users/jorian/PycharmProjects/algorithm/homeworks/lesson6/task1.py
# FRAME: <frame at 0x0000000001E25BE0, file 'C:/Users/jorian/PycharmProjects/algorithm/homeworks/lesson6/task1.py',
# line 37, code two_less_1>, EVENT: call, ARG: None.
# FRAME: <frame at 0x0000000001E259F0, file 'C:/Users/jorian/PycharmProjects/algorithm/homeworks/lesson6/task1.py',
# line 68, code two_less_2>, EVENT: call, ARG: None.
# FRAME: <frame at 0x0000000001ED1610, file 'C:/Users/jorian/PycharmProjects/algorithm/homeworks/lesson6/task1.py',
# line 100, code two_less_3>, EVENT: call, ARG: None.
# FRAME: <frame at 0x0000000001ED1800, file 'C:/Users/jorian/PycharmProjects/algorithm/homeworks/lesson6/task1.py',
# line 132, code two_less_4>, EVENT: call, ARG: None.
# Исходные данные:
# Версия системы: MSWindows 6. Разрядность системы: win32. версия пайтона: 3.8.
# Размер памяти, занятый исходным списком: 9016.
# Function "two_less_1" begin
# Memory taken:
# list - 9016
# two minimals begin - 48
# cycle pointer - 28
# two minimals end - 56
# Function maximum memory size = 9100
# Function "two_less_2" begin
# Memory taken:
# list - 9016
# two minimals begin - 52
# cycle pointer - 28
# two minimals end - 56
# Function maximum memory size = 9100
# Function "two_less_3" begin
# Memory taken:
# list - 9016
# two minimals begin - 56
# cycle pointer - 28
# two minimals end - 56
# Function maximum memory size = 9100
# Function "two_less_4" begin
# Memory taken:
# list - 9016
# two minimals begin - 32
# cycle pointer - 28
# two minimals end - 56
# Function maximum memory size = 9100
#
# Process finished with exit code 0
