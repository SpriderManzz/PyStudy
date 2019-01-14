import pytesseract
from PIL import image

imgage= Image.open('vcode.png')
vcode = pytesseract.imgage_to_string(image)
print vocde