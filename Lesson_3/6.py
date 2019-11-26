"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""


import random
MAS = []

for i in range(15):
    MAS.append(random.randrange(-5, 15))
print(f'Список:\n{MAS}')

MIN_IND = MAS.index(min(MAS))
MAX_IND = MAS.index(max(MAS))

if MAX_IND > MIN_IND:
    res = MAX_IND - MIN_IND - 1
    print(f'Между минимальным и максимальным числом находится {res} элементов\n')
else:
    res = MIN_IND - MAX_IND - 1
    print(f'Между минимальным и максимальным числом находится {res} элементов\n')