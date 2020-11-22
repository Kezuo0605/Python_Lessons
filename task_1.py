"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""

import random
import timeit


def bubble(origlist):
    """Стандартнный подход"""
    n = 1
    while n < len(origlist):
        for i in range(len(origlist)-n):
            if origlist[i] < origlist[i+1]:
                origlist[i], origlist[i+1] = origlist[i+1], origlist[i]
        n += 1
    return origlist
"""Доработка"""
def bubble1(origlist):
    """Завершаем если нет совпадений"""
    n = 1
    k = 0
    while n < len(origlist):
        for i in range(len(origlist)-n):
            if origlist[i] < origlist[i+1]:
                origlist[i], origlist[i+1] = origlist[i+1], orig_list[i]
                k = 1
        if k == 0:
            break
        n += 1
    return origlist


orig_list = [random.randint(-100, 100) for i in range(1000)]

print(timeit.timeit("bubble(origlist[:])", setup="from __main__ import bubble, origlist", number=1000))

