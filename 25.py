# Известна масса в килограммах каждого предмета, загружаемого в автомобиль. Определить общую массу груза.

n = int(input('Введите количество предметов '))

sum = 0

for nom in range(n):
    a = int(input('Введите массу очередного предмета '))
    sum = sum + a

print('Общая масса всех предметов = ', sum)
