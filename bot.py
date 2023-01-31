import time
import logging


import telebot 
from telebot import types


TOKEN = '5793278590:AAGg_cpMSaMmgCOhCWNe9g0uJyfuzzdMnoY'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    a = f'Hello, {message.from_user.first_name}\n'
    mess = a + '/get_book' + '/системы_счисления' + '/int' + '/float' + '/string' + '/control_characters'
    bot.send_message(message.chat.id, mess, parse_mode='html')
    
    
@bot.message_handler(commands=['get_book'])
def get_book(message):
    doc = open('/Users/aleksandr/Desktop/Prostoy_Pyton.pdf', 'rb')
    bot.send_document(message.chat.id, doc)
    bot.send_document(message.chat.id, "FILEID")
    doc.close()
    
    
@bot.message_handler(commands=['системы_счисления'])
def sist(message):
    photo = open('/Users/aleksandr/Documents/Programming/Python/telegran_python_guide_bot/Системы счисления/picture.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    
    
@bot.message_handler(commands=['int'])
def _int_(message):
    photo = open('/Users/aleksandr/Documents/Programming/Python/telegran_python_guide_bot/int/Без имени-1.png', 'rb')
    bot.send_photo(message.chat.id, photo)

    
@bot.message_handler(commands=['float'])
def _float_(message):
    photo = open('/Users/aleksandr/Documents/Programming/Python/telegran_python_guide_bot/float/Без имени-1.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    
    
@bot.message_handler(commands=['string'])
def _str_(message):
    photo1 = open('/Users/aleksandr/Documents/Programming/Python/telegran_python_guide_bot/string/Без имени-1.png', 'rb')
    bot.send_photo(message.chat.id, photo1)
    photo2 = open('/Users/aleksandr/Documents/Programming/Python/telegran_python_guide_bot/string/Без имени-2.png', 'rb')
    bot.send_photo(message.chat.id, photo2)
    photo3 = open('/Users/aleksandr/Documents/Programming/Python/telegran_python_guide_bot/string/Без имени-3.png', 'rb')
    bot.send_photo(message.chat.id, photo3)
    photo4 = open('/Users/aleksandr/Documents/Programming/Python/telegran_python_guide_bot/string/Без имени-4.png', 'rb')
    bot.send_photo(message.chat.id, photo4)
    
    
@bot.message_handler(commands=['control_characters'])
def contr(message):
    photo = open('/Users/aleksandr/Documents/Programming/Python/telegran_python_guide_bot/Управляющие символы/Без имени-1.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    
    
    
bot.polling(non_stop=True)
