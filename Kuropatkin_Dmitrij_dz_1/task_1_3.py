percent_1 = 'процент'  # задаем переменные для печати слова
percent_2 = 'процента'
percent_3 = 'процентов'

i = 0  # счетчик начала
numbers = {11, 12, 13, 14}
for i in range(100):  # пишем цикл for для печати результат с разным склонением
    i += 1
    if i in numbers:
        print(i, percent_3)
    elif i % 10 == 1:
        print(i, percent_1)
    elif 1 < i % 10 < 5:
        print(i, percent_2)
    else:
        print(i, percent_3)

