import qrcode

from PIL import Image

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10,
                   border=3) # Replace box-size & border with desire box size & border thickness

qr.add_data("https://kunal-khairnar-05.github.io/Portfolio/") # Enter your desire data that should be put into qrcode
qr.make(fit=True)

img = qr.make_image(fill_color="red",back_color="white") # fill_color for the qrcode color & back_color for background color

img.save("portfolio2.png") # replace the "portfolio2.png" with your desire file name
