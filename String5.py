# Задача 3. Определить позицию (номер) первого вхождения некоторого символа в заданную строку (если этого символа в
# строке нет, то вывести соответствующее сообщение).

st = input('Введите строку ')
sim = input('Введите символ ')
ind = st.find(sim)  # Функция fnd() вызывается как метод

if ind != -1:
    print(ind + 1)
else:
    print("NONE")
