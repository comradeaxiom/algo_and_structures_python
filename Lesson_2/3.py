"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
"""

NUMB = int(input("Введите число: "))
RES = 0
while NUMB > 0:
    RES = RES * 10 + NUMB % 10
    NUMB = NUMB // 10
print(RES)

"""
Рекурсия
"""

def rec_reverse(NUMB, rev=0):
    if NUMB == 0:
        return rev
    else:
        rev = int((rev + (NUMB %10) * 0.1) * 10)
        NUMB = NUMB // 10
        return rec_reverse(NUMB, rev)

