# 4.	Определить, какое число в массиве встречается чаще всего.

from random import randint

MAS = []
for i in range(15):
    MAS.append(randint(1, 10))
print(MAS)

VAR = 0
CNT = 0
for i in MAS:
    if MAS.count(i) > CNT:
        CNT = MAS.count(i)
        VAR = i
print(f"Чаще всего встречается {VAR}; {CNT} раз(а)")

