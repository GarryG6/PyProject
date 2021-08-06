# Определение m-й справа цифры числа

n = int(input('Введите натуральное число: '))
m = int(input('Введите номер цифры: '))

k = 0
while n > 0:
    posl = n % 10
    k = k + 1
    if k == m:
        print(posl)
    n = n // 10
