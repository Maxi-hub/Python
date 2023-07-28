'''
Напишите программу, которая получает целое число и возвращает его двоичное, восьмеричное строковое представление.
Функции bin и oct используйте для проверки своего результата. 
*Дополнительно 
Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления. Избегайте магических чисел.
Добавьте аннотацию типов где это возможно. Используйте функции
'''


def get_number() -> int:
    number = int(input("Введите число: "))
    return number

number = get_number()

def get_binary_number(number: int) -> list:
    list1 = []
    remainder = 0
    while number > 0:
        new_number = number // 2
        remainder = number % 2
        number = new_number 
        list1.append(remainder)
    return list1

list2 = get_binary_number(number)

def list_flip(list: list) -> list:
    for i in range(len(list2) // 2): # перемещение конечного элемента списка на начальный и наоборот, доходя до середины списка 
        list2[i], list2[len(list2)-1-i] = list2[len(list2)-1-i], list2[i]
    return list2

list2 = list_flip(list2)

binary_number = int(''.join(map(str, list2)))
print(f"Число в двоичной системе представления: {binary_number}") 

print(bin(number))


'''
Для перевода из двоичной в восьмеричную систему разбиваем двоичное число на группы по 3 цифры справа налево. 
В последней (самой левой) группе вместо недостающих цифр ставим слева нули.
'''
while len(list2)%3 != 0: # дополняем список нулями
    list2.insert(0, 0)

new_list = []
for i in range(0, len(list2), 3):
    one = list2[i]*(2**2)
    two = list2[i+1]*(2**1)
    three = list2[i+2]*(2**0)
    res = one + two + three
    new_list += {res}

octal_number = int(''.join(map(str, new_list)))
print(f"Число в восьмеричной системе представления: {octal_number}") 

print(oct(number))


