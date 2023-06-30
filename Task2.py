# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент
# к заданному числу X. Пользователь в первой строке вводит натуральное число
# N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     6
#     -> 5

import random
n = int(input('Введите количество элементов в массиве:'))
x = int(input('Введите число х: '))
arrow = []
for i in range(n):
    arrow.append(random.randrange(n))
print(arrow)
def nearval(arrow, number):
    return min(arrow, key=lambda x: abs(number - abs(x)))
print(f'Ближайшее к {x} число в массиве: {nearval(arrow, x)}')