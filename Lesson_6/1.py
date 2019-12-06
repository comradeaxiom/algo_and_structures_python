"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков. Проанализировать
результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде
комментариев к коду. Также укажите в комментариях версию Python
и разрядность вашей ОС.
"""

# Python ver. 3.7.4
# Win 10 Pro - 64


from memory_profiler import profile

@profile
def reverse_numb(numb):
	str_n = str(numb)
	length = len(str_n)
	r_numb = ''
	for i in range(length):
		r_numb = r_numb + r_numb.join(str_n[length-1])
		length -= 1
	print(r_numb)


while True:
	try:
		NUMB = int(input('Введите число: '))
		break
	except:
		print('Нужно ввести число!')


reverse_numb(NUMB)

'''
Line #    Mem usage    Increment   Line Contents
================================================
    15     13.2 MiB     13.2 MiB   @profile
    16                             def reverse_numb(numb):
    17     13.2 MiB      0.0 MiB   	str_n = str(numb)
    18     13.2 MiB      0.0 MiB   	length = len(str_n)
    19     13.2 MiB      0.0 MiB   	r_numb = ''
    20     13.2 MiB      0.0 MiB   	for i in range(length):
    21     13.2 MiB      0.0 MiB   		r_numb = r_numb + r_numb.join(str_n[length-1])
    22     13.2 MiB      0.0 MiB   		length -= 1
    23     13.2 MiB      0.0 MiB   	print(r_numb)
'''


from collections import namedtuple

@profile()
def company():
    n = int(input("Колличество предприятий: "))
    COMPANIES = namedtuple("company", "name kv_01 kv_02 kv_03 kv_04")
    PROFIT = {}

    for i in range(n):
         Company = COMPANIES(
            name=input("Название предприятия: "),
            kv_01=int(input("Выручка за 1-й квартал: ")),
            kv_02=int(input("Выручка за 2-й квартал: ")),
            kv_03=int(input("Выручка за 3-й квартал: ")),
            kv_04=int(input("Выручка за 4-й квартал: "))
         )
         PROFIT[Company.name] = int(Company.kv_01 + Company.kv_02 + Company.kv_03 + Company.kv_04)

    TOTAL = 0
    for value in PROFIT.values():
        TOTAL += value
    TOTAL = TOTAL / n


    for key, value in PROFIT.items():
        if value > TOTAL:
            print(key, " - прибыль выше среднего")
        if value < TOTAL:
            print(key, " - прибыль ниже среднего")
        if value == TOTAL:
            print(key, " - средняя прибыль")

company()

'''
Line #    Mem usage    Increment   Line Contents
================================================
    39     13.3 MiB     13.3 MiB   @profile()
    40                             def company():
    41     13.3 MiB      0.0 MiB       n = int(input("Колличество предприятий: "))
    42     13.3 MiB      0.0 MiB       COMPANIES = namedtuple("company", "name kv_01 kv_02 kv_03 kv_04")
    43     13.3 MiB      0.0 MiB       PROFIT = {}
    44                             
    45     13.4 MiB      0.0 MiB       for i in range(n):
    46     13.3 MiB      0.0 MiB            Company = COMPANIES(
    47     13.4 MiB      0.0 MiB               name=input("Название предприятия: "),
    48     13.4 MiB      0.0 MiB               kv_01=int(input("Выручка за 1-й квартал: ")),
    49     13.4 MiB      0.0 MiB               kv_02=int(input("Выручка за 2-й квартал: ")),
    50     13.4 MiB      0.0 MiB               kv_03=int(input("Выручка за 3-й квартал: ")),
    51     13.4 MiB      0.0 MiB               kv_04=int(input("Выручка за 4-й квартал: "))
    52                                      )
    53     13.4 MiB      0.0 MiB            PROFIT[Company.name] = int(Company.kv_01 + Company.kv_02 + Company.kv_03 + Company.kv_04)
    54                             
    55     13.4 MiB      0.0 MiB       TOTAL = 0
    56     13.4 MiB      0.0 MiB       for value in PROFIT.values():
    57     13.4 MiB      0.0 MiB           TOTAL += value
    58     13.4 MiB      0.0 MiB       TOTAL = TOTAL / n
    59                             
    60                             
    61     13.4 MiB      0.0 MiB       for key, value in PROFIT.items():
    62     13.4 MiB      0.0 MiB           if value > TOTAL:
    63     13.4 MiB      0.0 MiB               print(key, " - прибыль выше среднего")
    64     13.4 MiB      0.0 MiB           if value < TOTAL:
    65     13.4 MiB      0.0 MiB               print(key, " - прибыль ниже среднего")
    66     13.4 MiB      0.0 MiB           if value == TOTAL:
    67                                         print(key, " - средняя прибыль")
'''
# Нагрузки на память не замечено


@profile()
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

'''
Line #    Mem usage    Increment   Line Contents
================================================
   121     13.3 MiB     13.3 MiB   @profile()
   122                             def simple_num(ind):
   123     13.3 MiB      0.0 MiB       LST = [2]
   124     13.3 MiB      0.0 MiB       i = 3
   125     13.3 MiB      0.0 MiB       while len(LST) < ind:
   126     13.3 MiB      0.0 MiB           for j in LST:
   127     13.3 MiB      0.0 MiB               if i % j == 0:
   128     13.3 MiB      0.0 MiB                   break
   129                                     else:
   130     13.3 MiB      0.0 MiB               LST.append(i)
   131     13.3 MiB      0.0 MiB           i += 1
   132     13.3 MiB      0.0 MiB       return LST[ind - 1]
'''


@profile()
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

'''
Line #    Mem usage    Increment   Line Contents
================================================
   121     13.3 MiB     13.3 MiB   @profile()
   122                             def eratosfen(num):
   123     13.3 MiB      0.0 MiB       LST = [0] * 10000
   124     13.5 MiB      0.0 MiB       for i in range(10000):
   125     13.5 MiB      0.1 MiB           LST[i] = i
   126     13.5 MiB      0.0 MiB       LST[1] = 0
   127     13.5 MiB      0.0 MiB       IND = 2
   128     13.5 MiB      0.0 MiB       while IND < 10000:
   129     13.5 MiB      0.0 MiB           if LST[IND] != 0:
   130     13.5 MiB      0.0 MiB               j = IND * 2
   131     13.5 MiB      0.0 MiB               while j < 10000:
   132     13.5 MiB      0.0 MiB                   LST[j] = 0
   133     13.5 MiB      0.0 MiB                   j = j + IND
   134     13.5 MiB      0.0 MiB           IND += 1
   135     13.5 MiB      0.0 MiB       fin_lst = [el for el in LST if el != 0]
   136     13.5 MiB      0.0 MiB       return fin_lst[num - 1]
'''
# При решении задачи через решето проявляется незначительное прибавление памяти, в целом не влияющее
# на общую загруженность. Но при этом помним, что решето более эффективно по времени при больших
# вводных данных.