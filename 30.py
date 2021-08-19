# Дана последовательность чисел. Определить наибольшее количество подряд идущих одинаковых элементов
# этой последовательности.

n = int(input('Введите количество элементов '))

count = 1
max_ = 0

second = int(input('Введите элемент '))

for i in range(n - 1):
    first = int(input('Введите элемент '))

    if first == second:
        count = count + 1
    else:
        count = 0

    if count > max_:
        max_ = count

    second = first

print('Количество подряд идущих элементов = ', max_)
