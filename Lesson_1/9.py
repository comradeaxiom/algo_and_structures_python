# 9.Вводятся три разных числа. Найти, какое из них
# является средним (больше одного, но меньше другого).


VAR_1 = int(input("Первое число "))
VAR_2 = int(input("Второе число "))
VAR_3 = int(input("Третье число "))

if VAR_2 < VAR_1 < VAR_3 or VAR_3 < VAR_1 < VAR_2:
    print(f'Среднее: {VAR_1}')
elif VAR_1 < VAR_2 < VAR_3 or VAR_3 < VAR_2 < VAR_1:
    print(f'Среднее: {VAR_2}')
else:
    print(f'Среднее: {VAR_3}')

