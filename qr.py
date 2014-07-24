#!/usr/local/bin/python
import qrcode
from PIL import Image

ways = raw_input('from file, enter 1; from text, enter 2: ')

if ways == '1':
    input = raw_input('input the filename to be chaned here: ')
    f = open(input)
    file = f.read()

else:
    file = raw_input('text to change: ') 

output = raw_input('output filename: ')+ '.png'

qr = qrcode.QRCode(
    version=2,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=10,
    border=1
)
qr.add_data(file)
qr.make(fit=True)
img = qr.make_image()
file.close()


iconadd = raw_input('need an icon? y/n: ')

if iconadd =='n':
    img.save(output)

else:
    img = img.convert("RGBA")
    iconfile = raw_input('enter the icon filename: ') 
    icon = Image.open(iconfile)
 
    img_w, img_h = img.size
    factor = 4
    size_w = int(img_w / factor)
    size_h = int(img_h / factor)
 
    icon_w, icon_h = icon.size

    if icon_w > size_w:
        icon_w = size_w
    if icon_h > size_h:
        icon_h = size_h
    icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)
    icon = icon.convert("RGBA")
 
    w = int((img_w - icon_w) / 2)
    h = int((img_h - icon_h) / 2)
    img.paste(icon, (w, h), icon)
    img.save(output)
