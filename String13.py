# Задача 11. Дано предложение, в котором слова разделены одним пробелом (начальных и конечных пробелов нет).
# Получить и вывести на экран два его первых слова.

st = input('Введите предложение: ')
# Формируем первое слово
word1 = ''  # Начальное значение формируемого слова
num = 0
while st[num] != ' ':
    word1 = word1 + st[num]
    num = num + 1
# Встретился пробел - первое слово закончилось
# Печатаем его
print('Первое слово предложения: ', word1)
# Пропускаем пробел
num = num + 1
# Аналогично формируем второе слово
word2 = ''  # Начальное значение
while st[num] != ' ':
    word2 = word2 + st[num]
    num = num + 1
print('Второе слово предложения: ', word2)
