'''
Напишите рекурсивную программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. 
Приоритет операций стандартный.
*Пример:* 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;
- Добавьте возможность использования скобок, меняющих приоритет операций. Тут может помочь библиотека re.
*Пример:* 1+2*3 => 7; (1+2)*3 => 9;
'''

#list_1 = str(input("Введите арифметическое выражение, используя +,-,/,* (без =): "))

def math_expression(*args):
    res = ''
    for i in args:
        res += i
    return (res.split(" "))

math_expression_result = print(math_expression())

# def get_result(list_1):
#     for i in list_1:
#         a = int(''.join(map(str, list_1)))
#         print(a)
#         print(*str(a), sep=',')
   
  

# get_result(list_1)



