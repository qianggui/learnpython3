#!/usr/bin/env python3
# -*- conding:utf-8 -*-

from PIL import Image, ImageFilter
##pillow库可以实现图片切片、旋转、滤镜、输出文字、调色板等一应俱全

##打开一个jpg图像，注意当前啊路径
im = Image.open('dog.jpg')
##获取图像的尺寸
w, h = im.size
print('Original image size: %sx%s' % (w, h))
##缩放50%
im.thumbnail((w//2, h//2))
print('Resize image to: %sx%s' % (w//2, h//2))
##把缩放后的图像用jpeg格式保存
im.save('thumbnail.jpeg', 'jpeg')

print('\n---------------华丽的分割线--------------\n')

##使图片变模糊
im2 = Image.open('dog.jpg')
##应用模糊滤镜
im3 = im2.filter(ImageFilter.BLUR)
im3.save('blur.jpg', 'jpeg')

from PIL import ImageDraw, ImageFont
import random

##随机字母
def rndChar():
    return chr(random.randint(65, 90))

##随机颜色1
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

##随机颜色2
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

##240 x 60
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
##创建Font对象
font = ImageFont.truetype('Arial.ttf', 36)
##创建Draw对象
draw = ImageDraw.Draw(image)
##填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
##输出文字
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
##模糊
image = image.filter(ImageFilter.BLUR)
image.save('code.jpeg', 'jpeg')