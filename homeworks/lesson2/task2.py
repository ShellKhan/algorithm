# Задание 3.
# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.

def myrev(num: int, anti: int) -> int:
    anti = anti * 10 + num % 10
    num //= 10
    if num:
        return myrev(num, anti)
    else:
        return anti


num = int(input('Введите натуральное число: '))
print(f"Обратное число - {myrev(num, 0)}")
