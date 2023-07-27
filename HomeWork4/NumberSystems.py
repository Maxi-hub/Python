'''
Напишите программу, которая получает целое число и возвращает его двоичное, восьмеричное строковое представление.
Функции bin и oct используйте для проверки своего результата. 
*Дополнительно 
Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления. Избегайте магических чисел.
Добавьте аннотацию типов где это возможно. Используйте функции
'''


def get_number():
    number = int(input("Введите число: "))
    return number

number = get_number()

def get_binary_number(number: int):
    list1 = []
    remainder = 0
    while number > 0:
        new_number = number // 2
        remainder = number % 2
        number = new_number 
        list1.append(remainder)
    return list1

list2 = get_binary_number(number)

def list_flip(list: list):
    for i in range(len(list2) // 2): # перемещение конечного элемента списка на начальный и наоборот, доходя до середины списка 
        list2[i], list2[len(list2)-1-i] = list2[len(list2)-1-i], list2[i]
    return list2

list2 = list_flip(list2)

binary_number = int(''.join(map(str, list2)))
print(f"Число в восьмеричной системе представления: {binary_number}") 

print(bin(number))


