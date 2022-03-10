from PIL import Image, ImageFont, ImageDraw 

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
