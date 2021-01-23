# Задание 1.
# Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка. Требуется
# вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.
# Подсчет ведется двумя способами с использованием наиболее экономных методов. Результативность способов сравнивается.
# Поскольку в ходе разработки были сбои, я вывел не только количество подстрок, но и их списки, чтобы иметь возможность
# перепроверить вручную.
# Результаты сохранены в файле report.txt

import random
import hashlib
import sys
import timeit as tt

# За исходник берем строку символов, которые будут использоваться в измерениях. Я взял строчные латинские, но вообще
# можно любые. Создаем список вариантов длины для сравнительных измерений. Создаем пустой список для замеров памяти.
MEASURE_STRING = "abcdefghijklmnopqrstuvwxyz"
SIZES = [5, 10, 15, 20, 25, 50, 100]
report = None

# Константы измерений
VERSION_STR = 'Версия системы: MSWindows ' + str(sys.getwindowsversion().major)
BIT_DEPTH_STR = 'Разрядность системы: ' + sys.platform
PYTHON_STR = 'версия Python: ' + sys.winver


class SumMemory:
    """
    Класс для измерения памяти, позаимствован с небольшими изменениями из решения домашнего задания 6.
    """

    def __init__(self, name):
        """
        _sum_memory - общее количество занятой памяти
        _types - словарь вида {'type': [count, size]}
        name - название или описание измерения
        """
        self.name = name
        self._sum_memory = 0
        self._types = {}

    def extend(self, *args):
        for obj in args:
            self._add(obj)

    def _add(self, obj):
        spam = sys.getsizeof(obj)
        self._sum_memory += spam
        eggs = type(obj)
        if eggs in self._types:
            self._types[eggs][0] += 1
            self._types[eggs][1] += spam
        else:
            self._types[eggs] = [1, 1]
            self._types[eggs][1] = spam
        if hasattr(obj, '__iter__'):
            if hasattr(obj, 'items'):
                for key, value in obj.items():
                    self._add(key)
                    self._add(value)
            elif not isinstance(obj, str):
                for item in obj:
                    self._add(item)

    def __str__(self):
        return f'Измерение "{self.name}".\nПеременные заняли в сумме {self._sum_memory} байт\n' + \
               '\n'.join([f'Объекты класса {key} в количестве {value[0]} заняли {value[1]} байт'
                          for key, value in self._types.items()])


def make_my_str(my_size: int) -> str:
    """
    Функция, создающая строку указанной длины из случайных латинских строчных символов. Используется для измерений.
    """
    return ''.join([MEASURE_STRING[random.randint(0, 25)] for _ in range(my_size)])


def substr_count_std(mystr: str, memo: bool = False) -> list:
    """
    Функция, считающая количество подстрок при помощи встроенных функций и типов Python
    """
    global report
    s_set = set()
    for s_len in range(1, len(mystr)):
        for s_start in range(len(mystr) - s_len + 1):
            s_set.add(mystr[s_start:s_start + s_len])
    if memo:
        mem_count_std = SumMemory('Стандарт ' + mystr)
        mem_count_std.extend(*locals())
        report = mem_count_std
    return list(s_set)


def substr_count_hash(mystr: str, memo: bool = False) -> list:
    """
    Функция, считающая количество подстрок при помощи сравнения хешей. При выявлении неуникальности подстроки она
    сбрасывается - таким образом из всех неуникальных строк будет учтена только одна, самая последняя. Учитывается, что
    подстроки разной длины явно не могут быть одинаковыми.
    """
    global report
    s_list = []
    for s_len in range(1, len(mystr)):
        for s_start in range(len(mystr) - s_len + 1):
            s_xmpl = mystr[s_start:s_start + s_len]
            h_xmpl = hashlib.sha1(s_xmpl.encode('utf-8')).hexdigest()
            s_flag = True
            for s_next in range(s_start + 1, len(mystr) - s_len):
                if h_xmpl == hashlib.sha1((mystr[s_next:s_next + s_len]).encode('utf-8')).hexdigest():
                    s_flag = False
                    break
            if s_flag:
                s_list.append(s_xmpl)
    if memo:
        mem_count_hash = SumMemory('Хэш ' + mystr)
        mem_count_hash.extend(*locals())
        report = mem_count_hash
    return s_list


with open("report.txt", "a", encoding="UTF-8") as f_obj:
    print(VERSION_STR, file=f_obj)
    print(BIT_DEPTH_STR, file=f_obj)
    print(PYTHON_STR, file=f_obj)
    print(f'\n', file=f_obj)
    for size in SIZES:
        my_string = make_my_str(size)
        print(f'Строка {my_string} длины {size}:\n', file=f_obj)
        s = substr_count_std(my_string, True)
        print(report, file=f_obj)
        print(f'Количество подстрок стандартным методом - {len(s)}', file=f_obj)
        print(','.join(s), file=f_obj)
        print(f'Время: {tt.timeit("substr_count_std(my_string)", number=1000, globals=globals())}\n', file=f_obj)
        s = substr_count_hash(my_string, True)
        print(report, file=f_obj)
        print(f'Количество подстрок через хэши - {len(s)}', file=f_obj)
        print(','.join(s), file=f_obj)
        print(f'Время: {tt.timeit("substr_count_hash(my_string)", number=1000, globals=globals())}\n', file=f_obj)

# Ну выводы тут однозначные, на строках до 100 от хэша никакой пользы, кроме вреда.
# Эксперимент с длинами строки больше 100 провалился, так как я не смог дождаться его окончания - слишком долго.
