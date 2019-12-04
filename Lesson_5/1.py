"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""

from collections import namedtuple


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