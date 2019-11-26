#5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.

import random
MAS = []

for i in range(15):
    MAS.append(random.randrange(-5, 15))

MIN_IND = MAS.index(min(MAS))


print(f'Список:\n{MAS}')
print(f'Максимальное отрицательное число {min(MAS)}, его индекс {MIN_IND}')
