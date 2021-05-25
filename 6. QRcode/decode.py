from pyzbar.pyzbar import decode
from PIL import Image 
# pip install pillow

img = Image.open("C:/Users/DELL/Desktop/Projects/Python/Python projects/6. QRcode/TestFolder/myQRcode.png")

result = decode(img)

print(result)