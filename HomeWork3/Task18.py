'''
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке
вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка
содержит число X.
5
1 2 3 4 5
6
-> 5
'''

import random

number_len = int(input("Введите длину массива "))

list_1 = []
i = 0
while i < number_len:
    n = random.randint(1, 20)
    i+=1
    list_1.append(n)
print(list_1)

list_1 = sorted(list_1) 
print(list_1)

k = int(input("Введите число "))

res = 0
min = 0
for i in list_1:
    if k == i:
        res = k
        break
    if k > i:
        min = i
        res = min
    if k < i: 
        res = i
        break
print(res)

     

       