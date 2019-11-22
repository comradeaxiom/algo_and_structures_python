"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""

NUMB = int(input('Введите количество элементов: '))
i = 0
RANGE_NUMBER = 1
SUM = 0
while i < NUMB:
    SUM += RANGE_NUMBER
    RANGE_NUMBER /= -2
    i += 1

print(f'Сумма {SUM}')