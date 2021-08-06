# Определение m-й слева цифры числа

n = int(input('Введите натуральное число: '))
m = int(input('Введите номер цифры: '))
k = 0
n2 = n

while n2 > 0:
    n2 = n2 // 10
    k = k + 1

for a in range(k-m+1):
    posl=n%10
    n=n//10

print(posl)