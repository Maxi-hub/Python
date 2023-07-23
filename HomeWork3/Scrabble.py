'''
Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. В случае с английским алфавитом очки 
распределяются так:
● A, E, I, O, U, L, N, S, T, R – 1 очко;
● D, G – 2 очка;
● B, C, M, P – 3 очка;
● F, H, V, W, Y – 4 очка;
● K – 5 очков;
● J, X – 8 очков;
● Q, Z – 10 очков.
А русские буквы оцениваются так:
● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
● Д, К, Л, М, П, У – 2 очка;
● Б, Г, Ё, Ь, Я – 3 очка;
● Й, Ы – 4 очка;
● Ж, З, Х, Ц, Ч – 5 очков;
● Ш, Э, Ю – 8 очков;
● Ф, Щ, Ъ – 10 очков.
Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается только одно слово, 
которое содержит либо только английские, либо только русские буквы.
Ввод: ноутбук
Вывод: 12
'''

k = (input("Введите слово "))

list_1 = {'a', 'e', 'i', 'o', 'u', 'l', 'n', 's', 't', 'r'}
list_2 = {'d', 'g'}
list_3 = {'b', 'c', 'm', 'p'}
list_4 = {'f', 'h', 'v', 'w', 'y'}
list_5 = {'k'}
list_8 = {'j', 'x'}
list_10 = {'q', 'z'}

rus_1 = {'а', 'в', 'е', 'и', 'н', 'о', 'р', 'с', 'т'}
rus_2 = {'д', 'к', 'л', 'м', 'п', 'у'}
rus_3 = {'б', 'г', 'ё', 'ь', 'я'} 
rus_4 = {'й', 'ы'}
rus_5 = {'ж', 'з', 'х', 'ц', 'ч'}
rus_8 = {'ш', 'э', 'ю'}
rus_10 = {'ф', 'щ', 'ъ'}

list_1 = list_1.union(rus_1)
list_2 = list_2.union(rus_2)
list_3 = list_3.union(rus_3)
list_4 = list_4.union(rus_4)
list_5 = list_5.union(rus_5)
list_8 = list_8.union(rus_8)
list_10 = list_10.union(rus_10)

sum = 0
i = 0
while i < len(k):
    for item in list_1:
        if k[i] == item:
            sum +=1
    for item in list_2:
        if k[i] == item:
            sum +=2
    for item in list_3:
        if k[i] == item:
            sum +=3
    for item in list_4:
        if k[i] == item:
            sum +=4
    for item in list_5:
        if k[i] == item:
            sum +=5
    for item in list_8:
        if k[i] == item:
            sum +=8
    for item in list_10:
        if k[i] == item:
            sum +=10
    i+=1
print(sum)


