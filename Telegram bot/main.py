import logging
from datetime import datetime

import telebot
from PIL import Image, ImageDraw, ImageFont
from telebot import types 
from types import InlineKeyboardButton, InlineKeyboardMarkup

Token = "5272300324:AAHCJ1VjTvXJ-RbLu5a71zq5u4lHqapDfzk"
bot = telebot.TeleBot(Token)

images_dir = 'C:/Users/Acer/Desktop/photo'

text = ''

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

def print_text_on_photo(file_path, text):
    font = ImageFont.truetype('D:\Python GoIteens\Pet-Project\Telegram bot\PlayfairDisplay-VariableFont_wght.ttf', 80)
    image = Image.open(file_path)

    draw = ImageDraw.Draw(image)
    width_image, height_image = image.size
    width_text, height_text = draw.textsize(text, font=font)
    draw.text(
        ((width_image - width_text) / 2, ((height_image / 10) * 9)),
        text,
        font=font,
        fill=(0, 0, 0, 0)
    )

    image.save(file_path)

@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = types.InlineKeyboardMarkup()
    en = types.InlineKeyboardButton(text="English",callback_data="en")
    ua = types.InlineKeyboardButton(text="Українська", callback_data="ua")
    ru = types.InlineKeyboardButton(text="Руский",callback_data="ru")
    keyboard.add(en,ua,ru)
    bot.send_message(message.chat.id, "Выберете язык(Chouse lenguage):", reply_markup=keyboard)
@bot.message_handler(commands=['photo'])
def text_on_photo(message):
    bot.send_message(message.chat.id, 'Введіть текст: ')

@bot.message_handler(content_types=['text'])
def get_text_on_photo(message):
    global text
    text = message.text
    bot.send_message(message.chat.id, "Відправте фото")

@bot.message_handler(content_types=['photo'])
def image(message) -> None:
    global text
    if text != '':
        bot.reply_to(message, "Сейчас наколдую")
        file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
        file_downloaded = bot.download_file(file_info.file_path)
        file_name = "{}_{}.jpg".format(datetime.now().strftime("%Y-%m-%d"), message.from_user.id)
        file_path = "{}/{}".format(images_dir, file_name)
        with open(file_path, 'wb') as file_new:
            file_new.write(file_downloaded)
        print_text_on_photo(file_path, text)
        photo = open(file_path, 'rb')
        bot.send_photo(message.chat.id, photo)
        text = ''
    else:
        bot.reply_to(message, "Ви не ввели текста який хочете додати на фото")


bot.infinity_polling()