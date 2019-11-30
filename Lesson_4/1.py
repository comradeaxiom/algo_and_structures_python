"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""

# Пример 2-3

#3.	Сформировать из введенного числа обратное по порядку входящих в него
#цифр и вывести на экран. Например, если введено число 3486,
# то надо вывести число 6843.

import cProfile
import sys
import timeit
import time as t


sys.setrecursionlimit(1000000)


def timer_dec(dec_func):
    def tmp(*arg):
        st_time = t.time() * 1000
        result = dec_func(*arg)
        time = t.time() * 1000 - st_time
        print(f"Время выполнения: {time:.9f} мс")
        return result
    return tmp


#@timer_dec
def rec_count(NUMB):
    RES = 0
    while NUMB > 0:
        RES = RES * 10 + NUMB % 10
        NUMB = NUMB // 10
    print(RES)


#@timer_dec
def rec_reverse(NUMB, rev=0):
    if NUMB == 0:
        return rev
    else:
        rev = float((rev + (NUMB %10) * 0.1) * 10)
        NUMB = NUMB // 10
        return rec_reverse(NUMB, rev)



print(f"rec_count {rec_count(34560**200)}")
print(10 * "---")
# Время выполнения: 1.001464844 мс
print(f"rec_reverse {rec_reverse(34560**200)}")
print(10 * "---")
# Время выполнения: 1.000732422 мс



cProfile.run("rec_count(34560**200)")
# 5 function calls in 0.002 seconds
cProfile.run("rec_reverse(34560**2000)")
# 5243 function calls (4 primitive calls) in 0.091 seconds



print(timeit.timeit("rec_count(34560**200)", number=1, setup="from __main__ import rec_count"))
# 0.0015569
print(timeit.timeit("rec_reverse(34560**200)", number=1, setup="from __main__ import rec_reverse"))
# 0.0015534


'''
По времени работы оба кода работают примерно одинаково,
но при профилировании видно что рекурсивная функция сильно проигрывает
Необходима оптимизация кода.

В рекурсивной функции пришлось заменить int на float. При прогоне программа не могла перевести 
число в целое.
'''


