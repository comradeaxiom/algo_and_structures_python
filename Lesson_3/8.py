"""
8.	Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и
записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""

MATRIX = []

for i in range(4):
    MATRIX.append([])
    SUM = 0
    for n in range(4):
        USR_NUMB = int(input(f'Введите элемент {i+1} строки и {n+1} столбца: '))
        SUM += USR_NUMB
        MATRIX[i].append(USR_NUMB)

    MATRIX[i].append(SUM)

for a in MATRIX:
    print(('{:>4d}' * 5).format(*a))