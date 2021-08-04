my_list = [12.64, 54, 43.1, 13, 95, 44.7, 56, 32.17, 43.1, 17, 66.6, 23.45]
new_list = []  # создадим новый список для задания
for i in my_list:
    if type(i) == float:
        price = str(i).split('.')  # если число вещественное тогда сплитим по .
        if int(price[1]) < 10:
            new_list.append(f'{price[0]} руб 0{price[1]} коп')  # если целое то добавляем в новый список цены
        else:
            new_list.append(f'{price[0]} руб {price[1]} коп')
    else:
        new_list.append(f'{i} руб 00 коп')
print(*new_list, sep=',')  # выводим на экран цены через запятую согдласно заданию

print(new_list, id(new_list))
new_list.sort()  # сортируем список по возрастанию и доказываем по id  что это один объект списка
print(new_list, id(new_list))

my_list_2 = sorted(new_list, reverse=True)  # сортируем список по убыванию цен
print(my_list_2)
print(my_list_2[:5])  # выводим первые самые высокие цены
