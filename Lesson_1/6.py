# 6.	Пользователь вводит номер буквы в алфавите. Определить, какая это буква.


try:
    NUM = int(input("Введите номер буквы: "))
    print(f"Номер соответствует букве: {chr(ord('a') + NUM - 1)}")
except:
    print("Необходимо ввести номер!")