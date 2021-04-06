import qrcode

data = "Names: ABIZERA Oreste"

img = qrcode.make(data)

img.save("C:/Users/DELL/Desktop/Projects/Python/Python projects/QRcode/TestFolder/myQRcode.png")