'''
Напишите программу, которая получает целое число и возвращает его двоичное, восьмеричное строковое представление.
Функции bin и oct используйте для проверки своего результата. 
*Дополнительно 
Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления. Избегайте магических чисел.
Добавьте аннотацию типов где это возможно. Используйте функции
'''


number = int(input("Введите число: "))

list1 = []
remainder = 0
while number > 0:
    new_number = number // 2
    remainder = number % 2
    number = new_number 
    list1.append(remainder)

for i in range(len(list1) // 2):
    list1[i], list1[len(list1)-1-i] = list1[len(list1)-1-i], list1[i]

binary_number = int(''.join(map(str, list1)))
print(binary_number) 

