def give_sign(x):  # функция для получения знака перед первым символом
    if x[0] in '+-':
        return x[0]


new_list = ['в', '5', 'часов ', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

i = 0
while i < len(new_list):  # используем while для преобразований в списке
    sign = give_sign(new_list[i])
    if new_list[i].isdigit() or (sign and new_list[i][1:].isdigit()):  # испол-ем isdigit для выборки цифровых значений
        if sign:
            new_list[i] = sign + new_list[i][1:].zfill(2)  # c помощью метода .zfill добавим нолики
        else:
            new_list[i] = new_list[i].zfill(2)

        new_list.insert(i, '"')  # а с помощью insert обернем числа в ковычки
        new_list.insert(i + 2, '"')
        i += 2
    i += 1

str_new_list = " ".join(new_list)  # и .join нам все приведет к конечному виду
print(str_new_list)
