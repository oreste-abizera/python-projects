from pyzbar.pyzbar import decode
from PIL import Image 
# pip install pillow

img = Image.open("C:/Users/DELL/Desktop/Projects/Python/Python projects/QRcode/TestFolder/myQRcode.png")

result = decode(img)

print(result)