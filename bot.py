import time
import logging


import telebot 
from telebot import types


TOKEN = '-'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    a = f'Hello, {message.from_user.first_name}\n'
    mess = (a 
    + '/get_book\n'
    + '/системы_счисления\n'
    + '/int\n'
    + '/float\n'
    + '/string\n'
    + '/управляющие_символы\n'
    + '/списки\n'
    + '/кортежи\n'
    + '/словари')
    bot.send_message(message.chat.id, mess, parse_mode='html')
    
    
@bot.message_handler(commands=['get_book'])
def get_book(message):
    bot.send_message(message.chat.id, 'please wait...', parse_mode='html')
    doc = open('/Users/aleksandr/Documents/Programming/Python/telegran_python_guide_bot/Prostoy_Pyton.pdf', 'rb')
    bot.send_document(message.chat.id, doc)
    doc.close()
    
    
@bot.message_handler(commands=['системы_счисления'])
def sist(message):
    photo1 = open('/Users/aleksandr/Documents/Programming/Python/telegran_python_guide_bot/sistem/picture.png', 'rb')
    bot.send_photo(message.chat.id, photo1)
    photo1.close()
    
    
    
@bot.message_handler(commands=['int'])
def _int_(message):
    photo = open('/Users/aleksandr/Documents/Programming/Python/telegran_python_guide_bot/int/picture.png', 'rb')
    bot.send_photo(message.chat.id, photo)

    
@bot.message_handler(commands=['float'])
def _float_(message):
    photo = open('/Users/aleksandr/Documents/Programming/Python/telegran_python_guide_bot/float/Picture.png', 'rb')
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
    photo = open('/Users/aleksandr/Documents/Programming/Python/telegran_python_guide_bot/control_symb/Picture.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    photo.close()
    
    
@bot.message_handler(commands=['списки'])
def lists(message):
    photo1 = open('/Users/aleksandr/Documents/Programming/Python/telegran_python_guide_bot/Lists/Pic1.png', 'rb')
    photo2 = open('/Users/aleksandr/Documents/Programming/Python/telegran_python_guide_bot/Lists/Pic2.png', 'rb')
    photo3 = open('/Users/aleksandr/Documents/Programming/Python/telegran_python_guide_bot/Lists/Pic3.png', 'rb')
    photo4 = open('/Users/aleksandr/Documents/Programming/Python/telegran_python_guide_bot/Lists/pic4.png', 'rb')
    msg = '''
    Списки служат для того, чтобы хранить объекты в определенном порядке, особенно если порядок или содержимое могут изменяться.'''
    bot.send_message(message.chat.id, msg, parse_mode='html')
    bot.send_photo(message.chat.id, photo1)
    bot.send_photo(message.chat.id, photo2)
    bot.send_photo(message.chat.id, photo3)
    bot.send_photo(message.chat.id, photo4)
    photo4.close()
    photo3.close()
    photo2.close()
    photo1.close()
    

@bot.message_handler(commands=['кортежи'])
def tuples(message):
    msg = '''
    Кортежи, как и списки, являются последовательностями произвольных элементов. 
В отличие от списков кортежи неизменяемы. '''
    bot.send_message(message.chat.id, msg, parse_mode='html')
    photo1 = open('/Users/aleksandr/Documents/Programming/Python/telegran_python_guide_bot/tuples/pic.png', 'rb')
    bot.send_photo(message.chat.id, photo1)
    photo1.close()
    
    
@bot.message_handler(commands=['словари'])
def dictionary(message):
    msg = 'Словари - изменяемая структура данных. Имеет вид - ключ : значние'
    bot.send_message(message.chat.id, msg, parse_mode='html')
    photo1 = open('/Users/aleksandr/Documents/Programming/Python/telegran_python_guide_bot/dictionary/pic1.png', 'rb')
    photo2 = open('/Users/aleksandr/Documents/Programming/Python/telegran_python_guide_bot/dictionary/pic2.png', 'rb')
    bot.send_photo(message.chat.id, photo1)
    bot.send_photo(message.chat.id, photo2)
    photo2.close()
    photo1.close()
    

bot.polling(non_stop=True)
