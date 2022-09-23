#Librerias a instalar 
#pip install qrcode
#pip install pillow
#python setup.py install

import qrcode
from PIL import Image
from PIL.Image import Resampling

Logo_link = 'loto.png'
logo = Image.open(Logo_link)

# taking base width
basewidth = 100

# adjust image size
wpercent = (basewidth/float(logo.size[0]))
hsize = int((float(logo.size[1])*float(wpercent)))

logo = logo.resize((basewidth, hsize), Resampling.LANCZOS)
QRcode = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)

dato = input('Ingresa URL: ')
nombre = input('Ingrese el nombre del QR: ')

qr = qrcode.QRCode(version = 1, error_correction = qrcode.ERROR_CORRECT_L, box_size = 10, border = 4)

qr.add_data(dato)

qr.make(fit = True)

img = qr.make_image(fill_color = 'black', back_color = 'white').convert('RGB')

# set size of QR code
pos = ((img.size[0] - logo.size[0]) // 2,
       (img.size[1] - logo.size[1]) // 2)
       
img.paste(logo, pos)

img.save(nombre +'.png')

print('Código Qr generado!')
