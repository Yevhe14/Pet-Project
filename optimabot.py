import telebot 
from telebot import types 
 
bot = telebot.TeleBot('5248916121:AAHq7bQhoyri9PJRAUZEL1oldwenoNihPCo')

@bot.message_handler(commands=['class'])
def class_select(message):
    markup = types.InlineKeyboardMarkup(row_width = 4)
    class1 = types.InlineKeyboardButton('1', callback_data = '1')
    class2 = types.InlineKeyboardButton('2', callback_data = '2')
    class3 = types.InlineKeyboardButton('3', callback_data = '3')
    class4 = types.InlineKeyboardButton('4', callback_data = '4')
    class5 = types.InlineKeyboardButton('5', callback_data = '5')
    class6 = types.InlineKeyboardButton('6', callback_data = '6')
    class7 = types.InlineKeyboardButton('7', callback_data = '7')
    class8 = types.InlineKeyboardButton('8', callback_data = '8')
    class9 = types.InlineKeyboardButton('9', callback_data = '9')
    class10 = types.InlineKeyboardButton('10', callback_data = '10')
    class11= types.InlineKeyboardButton('11', callback_data = '11')
    markup.add(class1,class2,class3,class4,class5,class6,class7,class8,class9,class10,class11)
    bot.send_message(message.chat.id,"Выберете свой клас:", reply_markup=markup)

@bot.message_handler(commands=['menu'])
def class_select(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Имя")
    item2=types.KeyboardButton("Поменять клас")
    item3=types.KeyboardButton("Связаться с разработчиком")
    item4=types.KeyboardButton("Помощь проекту")
    item5=types.KeyboardButton("Добавить работу")
    item6=types.KeyboardButton("Наш чат")
    item7=types.KeyboardButton("Ответы")
    markup.add(item1, item2, item3, item4, item5, item6, item7)
    bot.send_message(message.chat.id,'Меню',reply_markup=markup)

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.InlineKeyboardMarkup(row_width = 2)
    lenguage1 = types.InlineKeyboardButton('Українська  🇺🇦', callback_data = 'ukraine')
    lenguage2 = types.InlineKeyboardButton('Руский  🇷🇺', callback_data = 'russian')
    markup.add(lenguage1,lenguage2)
    bot.send_message(message.chat.id,"Выберете язык:", reply_markup=markup)


@bot.message_handler(commands=['button'])
def button(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    item = types.InlineKeyboardButton('Как дела?', callback_data='question_1')
    item2 = types.InlineKeyboardButton('Пока', callback_data='goodbye')
    markup.add(item, item2)
 
    bot.send_message(message.chat.id, 'Привет!', reply_markup=markup)
 
@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == 'question_1':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text= 'Дела отлично!')
        if call.data == 'goodbye':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text= 'Пока друг')
        if call.data == 'ukraine':#для украинского языка
            pass
        if call.data == 'russian':#для руского языка
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text= 'Руский язык был успешно выбран!\nДля продолжения /class')
        if call.data == '1' or call.data == '2' or call.data == '3' or call.data == '4' or call.data == '5' or call.data == '6' or call.data == '7' or call.data == '8' or call.data == '9' or\
        call.data == '10' or call.data == '11':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text= f'Вы выбрали: {call.data} клас\nОтлчно! Теперь вы можете смотреть ответы по контрольных любых уроков и много чего другого\nДля входв меню /menu')
        if call.data == 'Алгебра':
            markup = types.InlineKeyboardMarkup(row_width = 2)
            l1 = types.InlineKeyboardButton('Тест 1', callback_data = 'Тест 1')
            l2 = types.InlineKeyboardButton('Тест 2', callback_data = 'test_2')
            markup.add(l1, l2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text = f"{call.data}: ", reply_markup=markup)
        if call.data == 'Тест 1':
            markup = types.InlineKeyboardMarkup(row_width = 1)
            back = types.InlineKeyboardButton('Назад', callback_data = 'backer')
            markup.add(back)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text = f"{call.data}: \nОтветы: https://telegra.ph/Test-1-TEST-VO-VREMYA-RAZRABOTKI-02-16", reply_markup=markup)
        

@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text=="Ответы":
        markup = types.InlineKeyboardMarkup(row_width = 2)
        lesson1 = types.InlineKeyboardButton('Українська Мова', callback_data = 'Українська мова')
        lesson2 = types.InlineKeyboardButton('Алгебра', callback_data = 'Алгебра')
        markup.add(lesson1, lesson2)

        bot.send_message(message.chat.id,"Выберете урок:", reply_markup=markup)
 
 




bot.polling()