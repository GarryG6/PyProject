# Напишите программу, которая определяет, верно ли, что введенное число состоит из одинаковых цифр (как, например, 666);

a = int(input('Введите число: '))

eq = 1

first = a % 10

while a > 0:
    second = first
    first = a % 10
    a = a // 10
    if first != second:
        eq = 0
        print('Число не состоит из одинаковых цифр')
        break
if eq:
    print('Число состоит из одинаковых цифр')