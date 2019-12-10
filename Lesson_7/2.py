"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
"""

from random import randint

def merge_sort(list_numb):
    if len(list_numb) > 1:
        center = len(list_numb) // 2
        left = list_numb[:center]
        right = list_numb[center:]

        merge_sort(left)
        merge_sort(right)

        a, b, c = 0, 0, 0

        while a < len(left) and b < len(right):
            if left[a] > right[b]:
                list_numb[c] = left[a]
                a += 1
            else:
                list_numb[c] = right[b]
                b += 1
            c += 1

        while a < len(left):
            list_numb[c] = left[a]
            a += 1
            c += 1

        while b < len(right):
            list_numb[c] = right[b]
            b += 1
            c += 1
        return list_numb

list_numb = [randint(-100, 100) for _ in range(10)]

print(f'Исходный массив - {list_numb}')
merge_sort(list_numb)
print(f'Отсортированный массив - {list_numb}')