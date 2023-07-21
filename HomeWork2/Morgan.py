'''
Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. 
Теперь надо проверить ее практически, в цикле 100 раз прогоняем каждый раз генерируем случайное количество предикат от 3 до 15 
и конечно со случайным булевым значением и засекаем общее время выполнения программы юзаем библиотеки random и time предикаты
НЕ ЗАДАЕМ как целое число!

'''
import random
import time
start_time = time.time()


from random import choice
x = choice([True,False]) 
y = choice([True,False]) 
z = choice([True,False]) 
print(f"If x = {x}, y = {y}, z = {z}")


left = not(x or y or z) 
right = not x and not y and not z
res = left

i = 0
while i <= 100:
    if left == right:
        i += 1
print(f"Result: {res}")
    

print("Spent", time.time() - start_time, "seconds")

