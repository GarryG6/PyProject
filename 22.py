# Напишите программу, которая определяет, верно ли, что введенное число: содержит две одинаковые цифры, стоящие рядом (как, например, 35 510).

n = int(input('Введите число: '))

first = n % 10  # Первая цифра из набора
n = n // 10
coincidence = 0  # Совпадение двух одинаковых цифр подряд

while n > 0:
    second = first
    first = n % 10
    if first == second:
        coincidence = 1
        break
    n = n // 10

if coincidence:
    print('Содержит')
else:
    print('Не содержит')
