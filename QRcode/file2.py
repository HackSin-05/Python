import qrcode

from PIL import Image

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10,
                   border=3)

qr.add_data("https://kunal-khairnar-05.github.io/Portfolio/")
qr.make(fit=True)

img = qr.make_image(fill_color="red",back_color="white")

img.save("portfolio2.png")
