# 9.8. Определение номера минимальной цифры числа при счете справа налево

n = int(input('Введите натуральное число: '))

posl = n % 10               # Выделяем последнюю цифру
Min = posl                  # Принимаем её в качестве минимальной
nomer_min = 1               # а в качестве номера - 1
nomer = 1
n = n // 10

# Рассматриваем остальные цифры
while n > 0:
    nomer = nomer + 1       # Номер очередной обрабатываемой цифры
    posl = n % 10           # Выделяем последнюю цифру
    if posl < Min:          # Сравниваем и при необходимости
        Min = posl          # меняем значение Min,
        nomer_min = nomer   # а в качестве значения nomer_min
                            # принимаем номер текущей цифры nomer
    n = n // 10
print('Номер минимальной цифры заданного числа равен', nomer_min)