# Определить порядковый номер числа 25 в наборе из 15 заданных чисел.

nomer_znach = 0
n = 15
znach = 25
for nom in range(1, n + 1):
    # Ввод очередного числа а
    a = float(input('Введите очередное число '))
    if a == znach:  # Если встретилось заданное число znach
        nomer_znach = nom  # Если встретилось заданное число znach

# Вывод ответа
print('Номер числа ', nomer_znach)
