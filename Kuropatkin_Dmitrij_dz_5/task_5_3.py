from itertools import islice, zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Егор']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А']

result = (i for i in zip_longest(tutors, klasses) if len(tutors) > len(klasses))
""" смешаем списки пока длинная итерация не закончится """

print(type(result))  # докажем что генератор
print(*islice(result, 9))  # выведем нужный результат
print(list(islice(result, 3)))  # все исчерпано 
