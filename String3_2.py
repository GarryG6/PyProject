# Задача 1. Определить, сколько раз в заданной строке встречается некоторый символ.

st = input('Введите строку: ')
sim = input('Введите символ: ')

k = st.count(sim)

# Выводим ответ
if k > 0:
    print('Заданный символ встречается в строке', k, 'раз')
else:
    print('Такого символа нет')