'''
Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
в порядке
Ввод: пара-ра-рам рам-пам-папам па-ра-па-дам
Вывод:Парам пам-пам
'''
from functools import reduce

list_1 = (input("Введите стихотворение: ")).split()
print(list_1)

list_vowels = 'аеёийоуыэюя'
# count = sum(sum(word.count(vowel) for vowel in list_vowels) for word in list_1)
# print(count) 

def good_song(list_vowels, list_1):
    S = (sum(map((lambda x: list_vowels.count(i) for i in list_vowels), list_1)))
    print(S) 

good_song(list_vowels, list_1)

res =  count // len(list_1)

# a = "Парам пам-пам"
# b = "Пам парам"
# res = reduce(lambda x, y: a if (x == y) else b, list_2)
print(res)








