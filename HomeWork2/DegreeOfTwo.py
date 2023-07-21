'''
Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
10 -> 1 2 4 8
'''

number = int(input("Введите число "))
degree_of_two = 2
degree = 0
result = 0
while result <= number:
    result = degree_of_two ** degree
    degree +=1
    if result <= number:
        print(result)
