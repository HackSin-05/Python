import qrcode as qr

img = qr.make("https://kunal-khairnar-05.github.io/Portfolio/")

img.save("my_portfolio.png")