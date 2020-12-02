# Задание 9.
# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

def digsum(num: int) -> int:
    sum = 0
    while num > 0:
        dig = num % 10
        sum += dig
        num //= 10
    return sum


print('Вводите натуральные числа или 0 для завершения')
maxsum = 0
maxnum = 0
while True:
    n = int(input())
    if n == 0:
        break
    elif digsum(n) > maxsum:
        maxsum = digsum(n)
        maxnum = n
print(f"Сумма цифр {maxnum} равна {maxsum}")
