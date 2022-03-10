from PIL import Image, ImageFont, ImageDraw 



my_image = Image.open("D:\Python GoIteens\Pet-Project\Telegram bot\p1.png")

title_text = "PHOTO"

title_font = ImageFont.truetype('D:\Python GoIteens\Pet-Project\Telegram bot\PlayfairDisplay-VariableFont_wght.ttf', 40)


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

print_text_on_photo(my_image, title_text, title_font)