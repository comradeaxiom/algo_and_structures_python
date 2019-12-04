"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

from collections import deque

NUM_1 = deque(input("Введите первое число: "))
NUM_2 = deque(input("Введите второе число: "))


def hex_sum(NUM_1, NUM_2):
    NUM_1 = "".join([i for i in NUM_1])
    NUM_2 = "".join([i for i in NUM_2])
    SUM = hex((int(float.fromhex(NUM_1) + float.fromhex(NUM_2))))
    SUM = deque(SUM[2::].upper())
    print("Сумма: ", SUM)


def hex_mul(NUM_1, NUM_2):
    NUM_1 = "".join([i for i in NUM_1])
    NUM_2 = "".join([i for i in NUM_2])
    SUM = hex((int(float.fromhex(NUM_1) * float.fromhex(NUM_2))))
    SUM = deque(SUM[2::].upper())
    print("Произведение: ", SUM)

hex_sum(NUM_1, NUM_2)
hex_mul(NUM_1, NUM_2)