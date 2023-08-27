'''
Создать телефонный справочник с возможностью импорта и экспорта данных в # формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться в файле. 
1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
4. Использование функций. Ваша программа не должна быть линейной
Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести имя или фамилию, и Вы 
должны реализовать функционал для изменения и удаления данных.
'''

from random import *
import json

phone_book = {}

def save():
    with open("phone_book.json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(phone_book, ensure_ascii=False))
    # print("Контакт сохранен")

def load():
    # используем global phone_book или return phone_book
    with open("phone_book.json", "r", encoding="utf-8") as fh:
        phone_book = json.load(fh)
    return phone_book

def delite():
    name = input("Введите имя для удаления: ")
    if name in phone_book:
        del phone_book[name]
        print("Контакт удален")
        save() 
    else:
        print("Такое имя не найдено") 
    return phone_book

def find():
    name = input("Введите имя для поиска: ")
    if name in phone_book:
        print(name, phone_book[name])
    else:
        print("Такое имя не найдено") 

def change():
    print("Что будем менять? 1 - name, 2 - phone number1, 3 - phone number2, 4 - birthday, 5 - email")
    n = int(input("Введите число: "))
    if n == 1:
        name = input("Введите имя для изменения: ")
        if name in phone_book:
            new_name = input("Введите новое имя: ")
            phone_book[new_name] = phone_book[name]
            del phone_book[name]
            print(new_name, phone_book[new_name])
            save()
            # print(phone_book.update())
        else:
            print("Такое имя не найдено в телефонном справочнике") 
    if n == 2:
        name = input("Введите имя контакта ")
        if name in phone_book:
            new_phone_number = input("Введите новый номер телефона: ")
            phone_book[name]['phone_numbers'][0] = new_phone_number
            print(name, phone_book[name])
            save()
        else:
            print("Такое имя не найдено в телефонном справочнике") 
    if n == 3:
        name = input("Введите имя контакта ")
        if name in phone_book:
            new_phone_number = input("Введите новый номер телефона: ")
            phone_book[name]['phone_numbers'][1] = new_phone_number
            print(name, phone_book[name])
            save()
        else:
            print("Такое имя не найдено в телефонном справочнике") 
    if n == 4:
        name = input("Введите имя контакта ")
        if name in phone_book:
            new_birthday = input("Введите дату рождения: ")
            phone_book[name]['birth_day'] = new_birthday
            print(name, phone_book[name])
            save()
        else:
            print("Такое имя не найдено в телефонном справочнике") 
    if n == 5:
        name = input("Введите имя контакта ")
        if name in phone_book:
            new_email = input("Введите email: ")
            phone_book[name]['email'] = new_email
            print(name, phone_book[name])
            save()
        else:
            print("Такое имя не найдено в телефонном справочнике") 

while True:
    command = input("Введите команду: ")
    if command == "/add":
        name = input("Введите имя нового контакта: ")
        number0 = input("Введите 1й номер: ")
        number1 = input("Введите 2й номер: ")
        bithday = input("Введите ДР: ")
        mail = input("Введите email: ")
        phone_book.update({name: {"phone_numbers": [number0, number1], "birth_day": bithday, "email": mail}})
        print("Контакт создан")
        save()
    if command == "/save":
        save()
    if command == "/del":
        delite()
    if command == "/load":
        phone_book = load()
    if command == "/all":
        print("Список всех контактов:")
        print(phone_book)
    if command == "/find":
        find()
    if command == "/change":
        change()


        