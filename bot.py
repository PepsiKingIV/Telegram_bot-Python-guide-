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
    photo1 = open('/Users/aleksandr/Documents/Programming/Python/telegran_python_guide_bot/sistem/picture.png', 'rb')
    bot.send_photo(message.chat.id, photo1)
    photo1.close()
    
    
    
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
    photo1 = open('/Users/aleksandr/Documents/Programming/Python/telegran_python_guide_bot/string/1.png', 'rb')
    bot.send_photo(message.chat.id, photo1)
    photo2 = open('/Users/aleksandr/Documents/Programming/Python/telegran_python_guide_bot/string/2.png', 'rb')
    bot.send_photo(message.chat.id, photo2)
    photo3 = open('/Users/aleksandr/Documents/Programming/Python/telegran_python_guide_bot/string/3.png', 'rb')
    bot.send_photo(message.chat.id, photo3)
    photo4 = open('/Users/aleksandr/Documents/Programming/Python/telegran_python_guide_bot/string/4.png', 'rb')
    bot.send_photo(message.chat.id, photo4)
    photo5 = open('/Users/aleksandr/Documents/Programming/Python/telegran_python_guide_bot/string/5.png', 'rb')
    bot.send_photo(message.chat.id, photo5)
    photo6 = open('/Users/aleksandr/Documents/Programming/Python/telegran_python_guide_bot/string/6.png', 'rb')
    bot.send_photo(message.chat.id, photo6)
    photo6.close()
    photo5.close()
    photo4.close()
    photo3.close()
    photo2.close()
    photo1.close()
    
    
@bot.message_handler(commands=['управляющие_символы'])
def contr(message):
    photo = open('/Users/aleksandr/Documents/Programming/Python/telegran_python_guide_bot/control_symb/Без имени-1.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    photo.close()
    
    
@bot.message_handler(commands=['списки'])
def contr(message):
    photo = open('', 'rb')
    bot.send_photo(message.chat.id, photo)
    
    
    
bot.polling(non_stop=True)
