import logging
from datetime import datetime

import telebot
from PIL import Image, ImageDraw, ImageFont
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

Token = "5272300324:AAHCJ1VjTvXJ-RbLu5a71zq5u4lHqapDfzk"
bot = telebot.TeleBot(Token)

images_dir = 'C:/Users/Acer/Desktop/photo'

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)


#func for add text on photo 
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
def image(message) -> None:
    '''processing incoming image'''
    bot.reply_to(message, "Сейчас наколдую")
    file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
    file_downloaded = bot.download_file(file_info.file_path)
    file_name = "{}_{}.jpg".format(datetime.now().strftime("%Y-%m-%d"), message.from_user.id)
    file_path = "{}/{}".format(images_dir, file_name)
    with open(file_path, 'wb') as file_new:
        file_new.write(file_downloaded)
    print_text_on_photo(file_path, "123")
    photo = open(file_path, 'rb')
    bot.send_photo(message.chat.id, photo)


bot.infinity_polling()