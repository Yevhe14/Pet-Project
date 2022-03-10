from PIL import Image, ImageFont, ImageDraw 



my_image = Image.open("D:\Python GoIteens\Pet-Project\Telegram bot\p1.png")

title_text = "PHOTO"

title_font = ImageFont.truetype('D:\Python GoIteens\Pet-Project\Telegram bot\PlayfairDisplay-VariableFont_wght.ttf', 100)


def print_text_on_photo(image, text, font_user):
    image_editable = ImageDraw.Draw(image)

    image_editable.text((15,15), text, (237,230,211), font=font_user)

    image.save('Result.jpg')

print_text_on_photo(my_image, title_text, title_font)