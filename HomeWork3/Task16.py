'''
Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит
натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
5
1 2 3 4 5
3
-> 1

'''

number_len = int(input("Введите число "))

list_1 = []
for i in range(number_len+1):
    list_1.append(i)
list_1.remove(0)
print(list_1)

x_number = (int(input("Введите искомое число ")))
count = 0
i = 0
while i < len(list_1):
    if list_1[i] == x_number:
        count +=1
    i+=1
print(count)






