import qrcode

from PIL import Image
import qrcode.constants

qr = qrcode.QRCode(version=1, 
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10, border=10)

qr.add_data("https://github.com/manenilesh")
qr.make(fit=True)
img = qr.make_image(fill_color = "red", back_color = "white")
img.save("Color_nilesh_GitHub.png")

