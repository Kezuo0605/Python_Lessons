"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""

import random


def sort(list):

    if len(list) > 1:
        midland = len(list) // 2
        lhalf = list[:midland]
        rhalf = list[midland:]

        i = 0
        j = 0
        k = 0
        while i < len(lhalf) and j < len(rhalf):
            if lhalf[i] < rhalf[j]:
                list[k] = lhalf[i]
                i = i + 1
            else:
                list[k] = rhalf[j]
                j = j + 1
            k = k + 1

        while i < len(lhalf):
            list[k] = lhalf[i]
            i = i + 1
            k = k + 1

        while j < len(rhalf):
            list[k] = rhalf[j]
            j = j + 1
            k = k + 1


n = int(input("Введите число элементов: "))
list = [random.random()*(100/2) for i in range(n)]

print(list)
sort(list)
print(list)