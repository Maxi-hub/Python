'''
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке
вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка
содержит число X.
5
1 2 3 4 5
6
-> 5
'''

number_len = int(input("Введите длину массива "))

list_1 = []
for i in range(number_len+1):
    list_1.append(i)
list_1.remove(0)
print(list_1)

x_number = (int(input("Введите число ")))
res = 0
if x_number > len(list_1):
    res = (len(list_1))
    print(res)
elif x_number < list_1[0]:
    res = (list_1[0])
    print(res)
else:
    res = x_number
    print(res)

