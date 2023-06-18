import qrcode as qr

img = qr.make("https://kunal-khairnar-05.github.io/Portfolio/") # Replace "https://kunal-khairnar-05.github.io/Portfolio/" with your desire location that you want to put into qrcode

img.save("my_portfolio.png") # Replace "my_portfolio.png" With your desire file name
