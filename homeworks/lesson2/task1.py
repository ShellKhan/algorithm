# Задание 2.
# Посчитать четные и нечетные цифры введенного натурального числа.

num = int(input('Введите натуральное число: '))
odd = even = 0
while True:
    c = num % 10
    if c % 2:
        odd += 1
    else:
        even += 1
    num = num // 10
    if num == 0:
        break
print(f"Четных цифр - {even}, нечетных - {odd}.")
