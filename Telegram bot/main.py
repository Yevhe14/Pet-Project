import logging

import telebot
from PIL import Image, ImageDraw, ImageFont
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

Token = "5272300324:AAHCJ1VjTvXJ-RbLu5a71zq5u4lHqapDfzk"
bot = telebot.TeleBot(Token)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)


#func for add text on photo 
def print_text_on_photo(image, text, font):
    draw = ImageDraw.Draw(image)
    width_image, height_image = image.size
    width_text, height_text = draw.textsize(text, font=font)
    draw.text(
        ((width_image - width_text) / 2, ((height_image / 10) * 9)),
        text,
        font=font,
        fill=(0, 0, 0, 0)
    )

    image.save('Result.jpg')

@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id,'Привет')

'''
@bot.message_handler(content_types=['document'])
def handle_docs_photo(message):
    try:
        chat_id = message.chat.id

        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        src = 'C:/Users/Acer/Desktop/photo/' + message.document.file_name;
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)

        bot.reply_to(message, "Додається текст")
    except Exception as e:
        bot.reply_to(message, "Сталася помилка!\
            \nСпробуйте знову")
'''

@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):

    try:
        chat_id = message.chat.id

        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        src='C:/Users/Acer/Desktop/photo/' + file_info.file_path;
        with open(src, 'wb') as new_file:
           new_file.write(downloaded_file)
        bot.reply_to(message,"Фото добавлено") 

    except Exception as e:
        bot.reply_to(message,e )

bot.infinity_polling()