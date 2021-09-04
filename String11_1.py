# Задача 9. Дана строка. Определить, образует ли число подстрока,начинающаяся с символа номер start и заканчивающаяся
# символом номер end.

st = input('Введите строку символов: ')
start = int(input('Введите номер начального символа подстроки: '))
end = int(input('Введите номер конечного символа подстроки: '))

substring = st[start - 1:end]
isNumber = True
for i in substring:
    if ord(i) < 48 or ord(i) > 57:
        isNumber = False

if isNumber:
    print('YES')
else:
    print('NONE')
