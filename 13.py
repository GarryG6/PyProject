# Дано натуральное число. Определить: номер минимальной цифры числа при счете слева направо (известно, что такая цифра – одна)

n = int(input('Введите натуралное число: '))

count = 0
n1 = n
while n1 > 0:
    n1 = n1 // 10
    count = count + 1
print(count)

min = n // 10 ** (count - 1)
pos = 1
res = pos
while pos < count:
    pos = pos + 1
    temp = n % 10 ** (count - pos + 1) // 10 ** (count - pos)
    if temp < min:
        min = temp
        res = pos

print(res)
