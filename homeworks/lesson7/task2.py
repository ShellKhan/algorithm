# Задание 2.
# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке
# [0; 50). Выведите на экран исходный и отсортированный массивы.
# Для генерации массива я использовал формулу random.random() * 50, поскольку random.uniform(0, 50) не гарантирует
# невключение правого края промежутка, как требуется по условию задачи.
# Размер массива уменьшен, так как более длинный трудно читать, а специально форматировать вывод не хочется.

import random

SIZE = 10
MAX_ITEM = 50


def merge_sorting(mylist: list) -> None:
    """
    Рекурсивное решение сортировки слиянием. При длине массива 2 или 1 мы его сортируем и возвращаем результат, при
    большей длине делим пополам и вызываем сортировку каждой части.
    В код википедии я заглядывал, но предпочел написать сам, поскольку мне не понравилось решение со склейкой и
    последующей перетасовкой списка. Аппенд быстрее и лишней памяти не жрет.
    """
    print(mylist)
    if len(mylist) == 2:
        if mylist[0] > mylist[1]:
            mylist[0], mylist[1] = mylist[1], mylist[0]
    elif len(mylist) > 2:
        part1 = mylist[:len(mylist) // 2]
        part2 = mylist[len(mylist) // 2:]
        merge_sorting(part1)
        merge_sorting(part2)
        mylist.clear()
        i = 0
        j = 0
        while True:
            if (i < len(part1)) and (j < len(part2)):
                if part1[i] < part2[j]:
                    mylist.append(part1[i])
                    i += 1
                else:
                    mylist.append(part2[j])
                    j += 1
            elif i < len(part1):
                mylist.append(part1[i])
                i += 1
            elif j < len(part2):
                mylist.append(part2[j])
                j += 1
            else:
                break
    print(mylist)


array = [random.random() * MAX_ITEM for _ in range(SIZE)]
merge_sorting(array)
