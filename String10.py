# Задача 8. Определить, есть ли в заданной строке некоторая подстрока.

st = input('Введите строку: ')
sim = input('Введите подстроку: ')
length1 = len(st)
length2 = len(sim)
k = 0

for i in range(length1 - length2 + 1):
    if st[i:i + length2] == sim:
        k = 1
        break

if k:
    print('YES')
else:
    print('NONE')
