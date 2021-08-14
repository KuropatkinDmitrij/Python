def odd_nums(num):
    for num in range(1, num + 1, 2):
        yield num


for i in odd_nums(30):
    print(i)


