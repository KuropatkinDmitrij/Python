from json import dump
from itertools import zip_longest

with open("users.csv", "r", encoding="utf-8") as users:  # открываем файлы из папки проекта
    with open("hobby.csv", "r", encoding="utf-8") as hobby:

        if len(users.readlines()) >= len(hobby.readlines()):
            users.seek(0)  # ставим указатель в начало двух списков
            hobby.seek(0)
            with open("dict.json", "w", encoding="utf-8") as f:  # создаем словарь
                main_list = zip_longest((" ".join(us.split(",")) for us in users), hobby, fillvalue=None)  # босс список
                my_dict = {str(el[0]).strip(): str(el[1]).strip() for el in main_list}  # формируем словарь

                dump(my_dict, f, ensure_ascii=False, indent=4)  # Сериализуем данные через функцию dump
            print(my_dict)
        else:
            exit(1)
