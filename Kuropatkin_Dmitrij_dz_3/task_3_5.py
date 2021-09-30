from random import choice, randrange

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def some_jokes(n, repeat=False):  # возвращаем случайные шутки, не повторяющиеся
    no, adv, adj = nouns.copy(), adverbs.copy(), adjectives.copy()  # копируем списки
    jokes = []
    list_min = min(no, adv, adj)
    while n and len(list_min):
        number = randrange(len(list_min))  # достаем случайный элемент
        if repeat:
            jokes.append(f"{no.pop(number)} {adv.pop(number)} {adj.pop(number)}")  # тут добв. фиксируемые элементы
        else:
            jokes.append(f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}")  # а тут добавляем своб-ую выборку
        n -= 1
    return jokes


print(some_jokes(7, True))
print(some_jokes(6, False))
