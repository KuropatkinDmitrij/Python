cubes = []  # создаем список кубов нечетных чисел
for i in range(1, 1000, 2):
    cubes.append(i ** 3)

sum_of_cubes = []  # создаем список сумм всех элементов
for element in cubes:
    new_sum = 0
    while element != 0:
        new_sum = new_sum + element % 10
        element = element // 10
    sum_of_cubes.append(new_sum)

new_numbers = []  # создаем список только тех чисел сумма которых делится нацело на 7
for i in range(len(sum_of_cubes)):
    if sum_of_cubes[i] % 7 == 0:
        new_numbers.append(cubes[i])

result_1 = 0  # находим результат для первой задачи
for i in range(len(new_numbers)):
    result_1 += new_numbers[i]

print('Задача а:', result_1)

for i in range(len(cubes)):  # добавим 17 к каждому элементу списка cubes
    cubes[i] = cubes[i] + 17

sum_of_cubes_2 = []  # опять создаем список сумм всех элементов
for element in cubes:
    new_sum = 0
    while element != 0:
        new_sum = new_sum + element % 10
        element = element // 10
    sum_of_cubes_2.append(new_sum)

new_numbers_2 = []  # опять создадим список только тех чисел которые нацело делится на 7
for i in range(len(sum_of_cubes_2)):
    if sum_of_cubes_2[i] % 7 == 0:
        new_numbers_2.append(cubes[i])

result_2 = 0  # найдем результат задачи
for i in range(len(new_numbers_2)):
    result_2 += new_numbers_2[i]

print('Задача b:', result_2)