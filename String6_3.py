# Задача 4. Определить, является ли символ строки с заданным номером цифрой.

st = input('Введите строку ')
num = int(input('Введите номер символа этой строки '))

num = num - 1  # для проверки значений символов в памяти следует уменьшить заданное значение num на 1

# Используем метод isdigit(). Этот метод проверяет, состоит ли строка из цифр, и возвращает логическое значение
if st[num].isdigit():
    print('Да, этот символ - цифра')
else:
    print('Нет, этот символ цифрой не является')
