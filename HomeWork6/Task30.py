'''
Задача 30: Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно 
ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1  + (n-1) * d.
Каждое число вводится с новой строки.
Ввод: 7 2 5
Вывод: 7 9 11 13 15
'''

a1 = int(input("Введите первый элемент арифметической прогрессии: "))
diff = int(input("Введите разность элементов: "))
number_of_elements = int(input("Введите количество элементов: "))

def progression(first_elememt: int, number_of_elements: int, difference: int):
    n = 1
    list_1 = []
    while len(list_1) < number_of_elements:
        a = a1 + ((n-1) * diff)
        list_1.append(a)
        n += 1
    print(*list_1)

progression(a1, number_of_elements, diff)