import qrcode

data = "Names: ABIZERA Oreste"

# this is the default QRCode
# img = qrcode.make(data)


# customizing qrcode

qr = qrcode.QRCode(version=1, box_size=10, border=5)

qr.add_data(data)

qr.make(fit=True)

img = qr.make_image(fill_color: 'red', back_color: 'white')

img.save("C:/Users/DELL/Desktop/Projects/Python/Python projects/QRcode/TestFolder/myQRcode.png")