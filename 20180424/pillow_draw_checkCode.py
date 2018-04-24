# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont, ImageFilter 
import random

#随机字母，注意ascii值
def rdChar():
    return chr(random.randint(65, 90))

#随机颜色
def rdColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

def rdColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

width = 240
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))

font = ImageFont.truetype('/usr/share/cups/fonts/FreeMono.ttf', 35)

draw = ImageDraw.Draw(image)

for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rdColor())

for t in range(4):
    draw.text((60 * t + 10, 10), rdChar(), font=font, fill=rdColor2())

image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')

