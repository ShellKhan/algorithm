# Задание 2.
# Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать на
# вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.

import math
import timeit
import cProfile

TIMEIT_COUNT = 10000


def range_prediction(num: int) -> int:
    """
    Прогнозируем размер массива от 1 до n, на котором ожидаем обнаружить num простых чисел по формуле "num <= n/ln(n)"
    Учитываем ошибку метода при num == 2
    :param num: int
    :return: int
    """
    if num in (1, 2):
        n = num + 1
    else:
        n = 2
        while (n / math.log(n)) < num:
            n += 1
    return n + 1


def eratosthenes_for(num: int) -> int:
    """
    Находим простое число с номером num методом решета Эратосфена с циклом for
    :param num: int
    :return: int
    """
    n = range_prediction(num)
    array = [i for i in range(n)]
    array[1] = 0
    for probe in range(2, n):
        if array[probe] != 0:
            pointer = probe * 2
            while pointer < n:
                array[pointer] = 0
                pointer += probe
    result = []
    for i in array:
        if array[i] != 0:
            result.append(array[i])
    return result[num - 1]


def eratosthenes_while(num: int) -> int:
    """
    Находим простое число с номером num методом решета Эратосфена с циклом while
    :param num: int
    :return: int
    """
    n = range_prediction(num)
    array = [i for i in range(n)]
    array[1] = 0
    probe = 2
    while probe < n:
        if array[probe] != 0:
            pointer = probe * 2
            while pointer < n:
                array[pointer] = 0
                pointer += probe
        probe += 1
    result = []
    for i in array:
        if array[i] != 0:
            result.append(array[i])
    return result[num - 1]


def dividers(num: int) -> int:
    """
    Находим простое число с номером num методом проверки делителей от 2 до N/2
    :param num: int
    :return: int
    """
    n = range_prediction(num)
    result = []
    for probe in range(n):
        if probe in (0, 1):
            continue
        elif probe in (2, 3):
            result.append(probe)
        else:
            for tester in range(2, math.floor(probe / 2) + 1):
                if probe % tester == 0:
                    break
            else:
                result.append(probe)
    return result[num - 1]


for num in (1, 2, 3, 4, 5, 10, 15, 20, 25, 30, 50, 75, 100, 150, 200, 250, 300, 500, 750, 1000):
    print(f'N = {num}')
    print(eratosthenes_for(num), end=' ')
    print(eratosthenes_while(num), end=' ')
    print(dividers(num))
    print(timeit.timeit('eratosthenes_for(num)', number=TIMEIT_COUNT, globals=globals()), end=' ')
    print(timeit.timeit('eratosthenes_while(num)', number=TIMEIT_COUNT, globals=globals()), end=' ')
    print(timeit.timeit('dividers(num)', number=TIMEIT_COUNT, globals=globals()))

cProfile.run('eratosthenes_for(10)')
cProfile.run('eratosthenes_for(100)')
cProfile.run('eratosthenes_for(1000)')
cProfile.run('eratosthenes_for(10000)')

cProfile.run('eratosthenes_while(10)')
cProfile.run('eratosthenes_while(100)')
cProfile.run('eratosthenes_while(1000)')
cProfile.run('eratosthenes_while(10000)')

cProfile.run('dividers(10)')
cProfile.run('dividers(100)')
cProfile.run('dividers(1000)')
cProfile.run('dividers(10000)')

print(timeit.timeit('range_prediction(10)', number=TIMEIT_COUNT, globals=globals()))
print(timeit.timeit('range_prediction(20)', number=TIMEIT_COUNT, globals=globals()))
print(timeit.timeit('range_prediction(30)', number=TIMEIT_COUNT, globals=globals()))
print(timeit.timeit('range_prediction(40)', number=TIMEIT_COUNT, globals=globals()))
print(timeit.timeit('range_prediction(50)', number=TIMEIT_COUNT, globals=globals()))
print(timeit.timeit('range_prediction(60)', number=TIMEIT_COUNT, globals=globals()))
print(timeit.timeit('range_prediction(70)', number=TIMEIT_COUNT, globals=globals()))
print(timeit.timeit('range_prediction(80)', number=TIMEIT_COUNT, globals=globals()))
print(timeit.timeit('range_prediction(90)', number=TIMEIT_COUNT, globals=globals()))
print(timeit.timeit('range_prediction(100)', number=TIMEIT_COUNT, globals=globals()))
print(timeit.timeit('range_prediction(150)', number=TIMEIT_COUNT, globals=globals()))

"""
В задаче сравниваются три алгоритма нахождения простых чисел: решето Эратосфена с циклом for, решето Эратосфена с циклом
while и метод проверки на делимость.
Сложность всех трех алгоритмов из рассмотрения кода предположительно квадратичная (цикл в цикле).
При этом дополнительное влияние оказывает функция предсказания необходимой длины массива, сложность которой
предположительно линейная.
    
Было проведено измерение скорости работы каждого из алгоритмов на наборе значений n:
1, 2, 3, 4, 5, 10, 15, 20, 25, 30, 50, 75, 100, 150, 200, 250, 300, 500, 750, 1000
- для каждого запущена функция timeit.timeit с числом повторов TIMEIT_COUNT, как рекомендовано в документации, 10000.
Установлено, что алгоритм 3 (проверка делителей) работает значительно медленнее, причем разрыв постоянно нарастает.
Вероятно тут играет роль постоянное уменьшение количества необнуленных элементов массива в алгоритмах 1 и 2, из-за чего
их сложность становится не квадратичной, а приблизительно линейно-логарифмической.  
Также удалось обнаружить различие в скорости работы циклов for и while. Начиная примерно с n = 20 цикл for устойчиво
показывает меньшее время работы.
Результаты, обработка и графики - в приложенном экселевском файле (лист "Задача 2").

Для функции предсказания длины массива были сделаны отдельные замеры на наборе значений n:
10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 150
- которые подтвердили ее линейную сложность.
Результаты и график - в приложенном экселевском файле (лист "Задача 2 - профилирование").

Также для каждого из алгоритмов выполнены вызовы под управлением функции cProfile.run для набора n:
10, 100, 1000, 10000.
Оснований для каких-либо ценных выводов это не дало.
Результаты - в приложенном экселевском файле (лист "Задача 2 - профилирование").
"""
