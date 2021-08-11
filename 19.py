# Даны натуральные числа a, b (a ≤ b, a > 1). Получить все простые числа pr, удовлетворяющие неравенствам a ≤ pr ≤ b.

a = int(input('Введите значение a: '))
b = int(input('Введите значение b: '))

first_n = a
if a % 2 == 0:
    first_n = a + 1

if a == 2:
    print(2)

for n in range(first_n, b + 1, 2):
    kol_del = 2
    vdel = 3
    while vdel * vdel <= n:
        if n % vdel == 0:
            kol_del = kol_del + 1
            break
        vdel = vdel + 2

    if kol_del == 2:  # Встретилось очередное простое число
        print(n)  # Печатаем его
