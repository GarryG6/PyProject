# Задача 1. Дано натуральное число n. Проверить, является ли оно простым.

n = int(input('Введите натуральное число: '))
kol_del = 1                         # Учитываем n в счетчике количества делителей

for vdel in range(1, n // 2 + 1):   # Рассматриваем возможные делители
    if n % vdel == 0:
        kol_del = kol_del + 1
# Проверяем
if kol_del == 2:
    print('Это число простое')
else:
    print('Это число простым не является')
