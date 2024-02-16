# pip install qrcode
import qrcode

# Get data from website URL
data = input("Enter URL: ")

# Get a name for png
picture_name = input("Enter a name for qrcode: ")

# Qr code effect
qr = qrcode.QRCode(version=1, box_size=10, border=5)

qr.add_data(data)

qr.make(fit=True)

img = qr.make_image(fill="black", back_color="white")

# Download qrcode image
img.save(picture_qrcode)
