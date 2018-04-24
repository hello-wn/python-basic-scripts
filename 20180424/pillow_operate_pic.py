# -*- coding: utf-8 -*-
from PIL import Image, ImageFilter

im = Image.open('origin.jpg')
w, h = im.size
print('Original image size: %s * %s' % (w, h))
#缩放到50%
im.thumbnail((w//2, h//2))
print('Resize image to %s * %s' % (w//2, h//2))
im.save('thumbnanail.jpg', 'jpeg')


im = Image.open('origin.jpg')
#应用模糊滤镜
im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg', 'jpeg')
