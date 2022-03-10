from PIL import Image, ImageFont, ImageDraw 

my_image = Image.open("D:\Python GoIteens\Pet-Project\Telegram bot\p1.png")

title_text = "The Beauty of Nature"

image_editable = ImageDraw.Draw(my_image)

title_font = ImageFont.truetype('D:\Python GoIteens\Pet-Project\Telegram bot\PlayfairDisplay-VariableFont_wght.ttf', 100)

image_editable.text((15,15), title_text, (237, 230, 211), font=title_font)

my_image.save("result.jpg")