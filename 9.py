# Дано натуральное число. Определить: сумму его четных цифр;

n = int(input('Введите натуральное число: '))
sum = 0
chet = False
posl = 0
while n > 0:
    posl = n % 10
    if chet:
        print(posl, end='  ')
        sum = sum + posl
        chet = False
    else:
        chet = True
    n = n // 10

print('Сумма всех четных чисел = ', sum)
