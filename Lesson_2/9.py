"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""

USR_NUMB = input("Введите числа через пробел: ")
NUM_SUM = 0
for i in USR_NUMB.split(' '):
    TMP_SUM = 0
    for li in i:
        TMP_SUM += int(li)
        if TMP_SUM >= NUM_SUM:
            NUM_SUM = TMP_SUM
            GR_NUM = i
print(f"Последнее введеное число наибольшее по сумме чисел: "
      f"{GR_NUM}, сумма его чисел: {NUM_SUM}")
