# pip install qrcode
import qrcode

# Get data from website URL
data = input("Enter URL: ")

# Qr code effect
qr = qrcode.QRCode(version=1, box_size=10, border=5)

qr.add_data(data)

qr.make(fit=True)

img = qr.make_image(fill="black", back_color="white")

# Download qrcode image
img.save("qrcode.png")
