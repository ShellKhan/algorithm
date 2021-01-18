# Задание 1.
# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке
# [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Размер 10 взят для большего удобства ручной проверки.

import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100


def extended_bubble_sorting(mylist: list) -> None:
    """
    В порядке усовершенствования ограничиваем сверху проходимый участок, так как последняя позиция в проходе становится
    упорядоченной. Другое усовершенствование - флаг перестановки. В начале цикла он сбрасывается, а при перестановке
    поднимается. Если флаг за время прохода не поднят, дальнейшая сортировка не требуется - массив уже упорядочен.
    На массиве длиной 10 это почти не заметно, но я проверял на массиве длиной 100, там при удачном раскладе может
    сэкономиться до 10 проходов.
    """
    nstep = 1
    shflag = True
    print(mylist)
    print('start!')
    while (nstep < len(mylist)) and shflag:
        shflag = False
        for i in range(len(mylist) - nstep):
            if mylist[i] < mylist[i + 1]:
                mylist[i], mylist[i + 1] = mylist[i + 1], mylist[i]
                shflag = True
        nstep += 1
        print(mylist)
    print('stop!')
    print(mylist)


array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
extended_bubble_sorting(array)
