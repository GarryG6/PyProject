# Задача 3. Найти 100 первых простых чисел.

print(2, end=' ')  # Первое простое число - 2
k = 1
n = 3  # Первое проверяемое число
while k < 100:
    kol_del = 2
    vdel = 3
    while vdel * vdel <= n:
        if n % vdel == 0:
            kol_del = kol_del + 1
            break
        vdel = vdel + 2
    if kol_del == 2:  # Встретилось очередное простое число
        print(n, end=' ')  # Печатаем его
        k = k + 1
    n = n + 2  # Следующее проверяемое нечетное число
