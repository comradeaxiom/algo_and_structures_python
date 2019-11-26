# 9.	Найти максимальный элемент среди минимальных элементов столбцов матрицы.


import random

MATRIX = []

for i in range(15):
    MATRIX.append([])
    MATRIX[i].extend([random.randint(0, 99) for _ in range(15)])

MIN_LIST = []
MIN_LIST.extend(MATRIX[0])

for string in MATRIX:
    print()
    print(('{:4d} ' * len(string)).format(*string))
    i = 0
    for j in string:
        if j < MIN_LIST[i]:
            MIN_LIST[i] = j
        i += 1

print()
print('min_list')
print(('{:4d} ' * len(MIN_LIST)).format(*MIN_LIST))
print()

MIN_LIST.sort(reverse=True)
print(
        'Максимальный элемент среди минимальных элементов столбцов матрицы: ',
        MIN_LIST[0]
            )