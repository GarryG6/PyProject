# Дана последовательность чисел. Определить наибольшую длину монотонного фрагмента последовательности (то есть такого
# фрагмента, где все элементы либо больше предыдущего, либо меньше). Принять, что в последовательности нет соседних
# одинаковых чисел. Задачу решите двумя способами:
# 1) с повторным вводом всех чисел последовательности;

n = int(input("Введите количество элементов последовательности: "))

Max = 0
Min = 0

count = 1
second = int(input('Введите элемент 1 '))
for i in range(n - 1):
    first = int(input('Введите элемент '))
    if first > second:
        count = count + 1
    else:
        count = 0
    if count > Max:
        Max = count
    second = first

count = 1
print('Повторный ввод')
second = int(input('Введите элемент 1 '))
for i in range(n - 1):
    first = int(input('Введите элемент '))
    if first < second:
        count = count + 1
    else:
        count = 0
    if count > Min:
        Min = count
    second = first

if Max > Min:
    print('Наибольшая длина последовательности = ', Max)
elif Min > Max:
    print('Наибольшая длина последовательности = ', Min)
else:
    print('Наибольшая длина последовательности = ', Max)
