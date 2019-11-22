"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""

NUMB = input('Введите число: ')
even = 0
odd = 0
for f in NUMB:
    i = int(f)
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print(f'У числа {NUMB}: четных цифр - {even}, нечетных - {odd} ')


"""
Решение через рекурсию
"""

def rec_count(numb, even=0, odd=0):
    if numb == 0:
        return even, odd
    else:
        if (numb % 10) % 2 == 0:
            even += 1
        else:
            odd += 1
        numb = numb // 10
        return rec_count(numb, even, odd)

