def thesaurus(*names):
    result_dict = {}  # создаем словарь
    for name in names:
        key = name[0].capitalize()  # определяем ключи
        if key not in result_dict:
            result_dict[key] = []  # отсекаем ненужные ключи
        result_dict[key].append(name)  # добавляем в словарь
    return result_dict  # возвращаем готовый словарь


print(thesaurus('Зухра', 'Гульчатай', 'Макс', 'Маша', 'Зина'))
