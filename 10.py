# «Дано натуральное число. Определить: количество его цифр, больших 5;

n = int(input('Введите простое число: '))

kol = 0
posl = 0
while n > 0:
    posl = n % 10
    if posl > 5:
        kol = kol + 1
    n = n // 10

print('Количество цифр больше 5 = ', kol)
