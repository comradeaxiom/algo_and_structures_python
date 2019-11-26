#3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.

from random import random

N = 5
ARG = [0] * N
for i in range(N):
    ARG[i] = int(random() * 100)
    print(ARG[i], end=' ')
print()


MN = min(ARG)
MX = max(ARG)
imn = ARG.index(MN)
imx = ARG.index(MX)
print('arr[%d]=%d arr[%d]=%d' % (imn + 1, MN, imx + 1, MX))
ARG[imn], ARG[imx] = ARG[imx], ARG[imn]

for i in range(5):
    print(ARG[i],end=' ')
print()
