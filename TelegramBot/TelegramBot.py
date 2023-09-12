import telebot  
from random import *
import json
import requests
from telebot import types
from dotenv import load_dotenv
import os

load_dotenv()
API_URL = 'https://7012.deeppavlov.ai/model'

bot = telebot.TeleBot(os.getenv('TOKEN'))


films = []
hello = ["привет", "добрый день", "добрый вечер", "здравств", "hi", "hello"]
good_mood = ["хорошо", "отлично", "замечательно", "лучше не бывает", "нормально"]
bad_mood = ["плохо", "не очень", "так себе", "отстой", "хуже не бывает"]


@bot.message_handler(commands = ['start'])
def start_message(message): 
        films.append("Interstellar")
        films.append("Inception")
        films.append("The Gentelmen")
        films.append("The Covenant")
        films.append("Sherlock Holmes") 
        bot.send_message(message.chat.id,"Фильмотека была загружена по умолчанию!")


@bot.message_handler(commands=['all'])
def show_all(message):
    try:
        bot.send_message(message.chat.id,"Вот список фильмов")
        bot.send_message(message.chat.id, ", ".join(films))
    except:
         bot.send_message(message.chat.id,"Фильмотека то пустая! Давай добавим что-нибудь.")


@bot.message_handler(func=lambda message: message.text == '/add')
def add_film(message):
    bot.send_message(message.chat.id, "Введите название фильма. После добавления не забудь его сохранить в коллекции.")
    bot.register_next_step_handler(message, process_new_film)

def process_new_film(message):
    new_film = message.text
    films.append(new_film)
    bot.send_message(message.chat.id, "Фильм добавлен в коллекцию!")

    

@bot.message_handler(commands=['save'])
def save_all(message):
    with open("films.json","w",encoding="utf-8") as fh:
        fh.write(json.dumps(films,ensure_ascii=False))
    bot.send_message(message.chat.id,"Фильмотека была успешно сохранена в файле films.json")


@bot.message_handler(func=lambda message: message.text == '/wiki')
def wiki(message):
    bot.send_message(message.chat.id,"Введите запрос")
    bot.register_next_step_handler(message, process_wiki_query)

def process_wiki_query(message):
    quest = message.text
    quest = message.text.split()[1:]
    qq=" ".join(quest)
    data = { 'question_raw': [qq]}
    try:
        res = requests.post(API_URL,json=data,verify=False).json()
        bot.send_message(message.chat.id, res)
    except:
        bot.send_message(message.chat.id, "Что-то я ничего не нашел :-(")


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
      
    for item in hello:
        if item in message.text.lower():
            bot.send_message(message.chat.id, "И я тебя приветствую! Поболтаем?")
            keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
            key_yes = types.InlineKeyboardButton(text='Конечно', callback_data='yes'); 
            keyboard.add(key_yes); 
            key_no= types.InlineKeyboardButton(text='Не сейчас', callback_data='no')
            keyboard.add(key_no)
            ansver = "Что скажешь?"
            bot.send_message(message.chat.id, text = ansver, reply_markup=keyboard)
            return
    
    if "дела" in message.text.lower():
        bot.send_message(message.chat.id, "Дела у меня хорошо, сам как?")
    elif any(word in message.text.lower() for word in good_mood):
        bot.send_message(message.chat.id, "Рад за тебя!")
    elif any(word in message.text.lower() for word in bad_mood):
        bot.send_message(message.chat.id, "It's gonna be okay. Don't worry, be happy!")
    else:
        bot.send_message(message.chat.id, "Моя твоя не понимать, давай еще что-нибудь.")


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes": #call.data это callback_data, которую мы указали при объявлении кнопки
        bot.send_message(call.message.chat.id, 'Отлично') #код сохранения данных, или их обработки
    elif call.data == "no":
        bot.send_message(call.message.chat.id, 'Может тогда позже. Ну ты, если что, заходи')

bot.polling(none_stop=True, interval=0) #запуск бота, кот.включает в себя скрытый цикл while true


