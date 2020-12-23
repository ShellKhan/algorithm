# Задание 1.
# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 числа) для
# каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести
# наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import namedtuple

qty = int(input('Введите количество предприятий: '))
Plant = namedtuple('Plant', 'name, profit_year')
plants = []
middle_profit = 0
for i in range(qty):
    name = input('Введите название предприятия: ')
    profit = []
    for j in range(4):
        profit.append(int(input(f'Введите прибыль за {j + 1} квартал: ')))
    plants.append(Plant(name=name, profit_year=sum(profit)))
for j in range(len(plants)):
    middle_profit += plants[j].profit_year
middle_profit /= qty
best = []
worst = []
average = []
for k in range(len(plants)):
    if plants[k].profit_year > middle_profit:
        best.append(plants[k].name)
    elif plants[k].profit_year < middle_profit:
        worst.append(plants[k].name)
    else:
        average.append(plants[k].name)
print(f'Средняя прибыль равна {round(middle_profit,2)}')
# Здесь я не стал усложнять вывод на случай, если в одном из списков окажется только одно наименование,
# и с согласованием грамматики возиться тоже не стал - единственно в силу нехватки времени,
# так что прошу за это строго не судить.
print(f'Хуже поработали {", ".join(worst):}')
print(f'Лучше поработали {", ".join(best):}')
if len(average):
    print(f'На среднем уровне оказались {", ".join(average):}')