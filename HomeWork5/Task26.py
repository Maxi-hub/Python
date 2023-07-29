'''
Задача 26: Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8
'''

def degree_of_number(a, b):
    if b == 1:
        return a 
    else:
        return a*degree_of_number(a, b - 1)
    
    
d = degree_of_number(2, 3)
print(d)

    