'''
Напишите рекурсивную программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. 
Приоритет операций стандартный.
*Пример:* 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;
- Добавьте возможность использования скобок, меняющих приоритет операций. Тут может помочь библиотека re.
*Пример:* 1+2*3 => 7; (1+2)*3 => 9;
'''
# import re

# list_1 = str(input("Введите арифметическое выражение, используя +,-,/,* (без =): "))
# regex = re.compile('.?')
# print(regex.findall(list_1))


list_1 = str(input("Введите арифметическое выражение, используя +,-,/,* (без =): "))
# list_2 = []
# for i in list_1:
#     list_2 += i
# print(*list_2)
# print(type(list_2))
# print(len(list_2))

def math_expression(list_1, index = 0):
    num = int(list_1[0]) 
    if num < 0:
        num -= 1
        return
    res = 0
    a = int(list_1[index]) 
    res += a
    print(res)
    return math_expression(list_1, index+1)

 
math_expression(list_1)
    

   

# list_1 = str(input("Введите арифметическое выражение, используя +,-,/,* (без =): "))
# def math_expression(expression):
#     m = ['+', '-', '/', '*']
#     new_list = []
#     for i in expression:
#         for j in m:
#             if i == j:
#                 return j
#             i+=1
#             return i
#         j+=1
#         new_list.append(j)
        
#     new_list.append(i) 
#     print(new_list)
        
    # if len(new_list) == 1:
    #     return new_list
    # return math_expression(expression)
            
  
# math_expression_result = print(math_expression(list_1))

# def math_expression(*args):
#     res = ''
#     for i in args:
#         res += i
#     return (res.split(" "))

# math_expression_result = print(math_expression(list_1))



# list_1 = str(3, '+', 2, '-', 1)
# sum = 0
# for i in list_1:
#     sum +=i
#     print(sum)


