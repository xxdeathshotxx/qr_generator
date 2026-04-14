import qrcode
from PIL import Image   // make sure you have already installed pillow library

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    border=4,
    box_size=10
)

qr.add_data("       paste") // paste your urls
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")      // you can change colour according to your wish

img.save("ww.png")        // choose any name to save your qr
img.show()   # 👈 this opens the image
