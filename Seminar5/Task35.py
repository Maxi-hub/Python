'''
Задача №35.Напишите функцию, которая принимает одно число и проверяет, является ли оно простым 
Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
Input: 5
Output: yes
'''

number = int(input("Введите число: "))

def simple_number(number, number2):
    if number <= 1:
        return True
    elif number2 % number == 0:
        return False
    
    return simple_number(number - 1, number2)


print(simple_number(number - 1, number))