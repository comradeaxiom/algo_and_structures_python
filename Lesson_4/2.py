"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
"""

import timeit
import cProfile


def simple_num(ind):
    LST = [2]
    i = 3
    while len(LST) < ind:
        for j in LST:
            if i % j == 0:
                break
        else:
            LST.append(i)
        i += 1
    return LST[ind - 1]
print(simple_num(1000))


def eratosfen(num):
    LST = [0] * 10000
    for i in range(10000):
        LST[i] = i
    LST[1] = 0
    IND = 2
    while IND < 10000:
        if LST[IND] != 0:
            j = IND * 2
            while j < 10000:
                LST[j] = 0
                j = j + IND
        IND += 1
    fin_lst = [el for el in LST if el != 0]
    return fin_lst[num - 1]
print(eratosfen(1000))

#cProfile.run("simple_num(10)")
# 18 function calls in 0.000 seconds
#cProfile.run("eratosfen(10)")
# 5 function calls in 0.006 seconds


#cProfile.run("simple_num(1000)")
# 8921 function calls in 0.038 seconds
#cProfile.run("eratosfen(1000)")
# 5 function calls in 0.006 seconds

#print(timeit.timeit("simple_num(5)", number=1, setup="from __main__ import simple_num"))
# 0.0002145
#print(timeit.timeit("eratosfen(5)", number=1, setup="from __main__ import eratosfen"))
# 2.1452147

#print(timeit.timeit("simple_num(1000)", number=1, setup="from __main__ import simple_num"))
# 0.0021322
#print(timeit.timeit("eratosfen(1000)", number=1, setup="from __main__ import eratosfen"))
# 0.006143599999999999

'''
Решение с использованием решетки Эратосфена проигрывает на малых вводных данных,
но показывает лучшие результаты при вычеслении больших данных
'''
