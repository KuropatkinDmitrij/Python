new_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for i in range(len(new_list)):  # Приводим все к нижнему регистру
    new_list[i].islower()

for i in range(len(new_list)):
    some_list = new_list[i].split(" ")  # разбиваем фразы на элементы
    name_indexes = len(some_list) - 1  # находим нужные индексы изменяемых имен
    some_name = some_list[name_indexes]  # Вынимаем имена из фраз
    name = some_name.title()   # Делаем заглавные буквы
    new_list.append(name)   # добавляем имена в конец списка

del new_list[0:4:1]  # с помощью среза удаляем ненужную часть списка

for words in new_list:  # C помощью цикла выводим нужные данные из конечного списка
    print('Привет,', words, '!')
