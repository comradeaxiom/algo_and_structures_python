"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""

from random import randint

def bubble_sort(list_numb):
    n = 1
    while n < len(list_numb):
        for i in range(len(list_numb)-n):
            if list_numb[i] < list_numb[i+1]:
                list_numb[i], list_numb[i+1] = list_numb[i+1], list_numb[i]
        n += 1
    return list_numb

list_numb = [randint(-100, 100) for _ in range(10)]

print(list_numb)

bubble_sort(list_numb)

print(list_numb)