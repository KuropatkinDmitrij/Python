new_dict = {"one": '"один"', "two": '"два"', "three": '"три"', "four": '"четыре"', "five": '"пять"', "six": '"шесть"',
            "seven": '"семь"', "eight": '"восемь"', "nine": '"девять"', "zero": '"ноль"'}


def num_translate(n):
    try:
        print(new_dict[n])
    except KeyError:
        print('None')


num_translate("one")
num_translate("two")
num_translate("nine")
num_translate("twenty")
num_translate("zero")
