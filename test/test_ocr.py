from PIL import Image    
import pytesseract

# /usr/local/Cellar/tesseract/4.0.0_1/bin/tesseract [for mac]
# /usr/share/tesseract-ocr/4.00/tessdata [for linux]

file_name = '/home/nilim/Documents/programmer/ocr-api/page_1.jpg'

ben = pytesseract.image_to_string(Image.open(file_name))
# ben = pytesseract.image_to_string(Image.open(file_name), lang='ben')
# ben2 = pytesseract.image_to_string(Image.open(file_name), lang='ben2')
# bengali = pytesseract.image_to_string(Image.open(file_name), lang='Bengali')


f = open("ben.txt", "w")
f.write(str(ben))
f.close()

# f = open("ben2.txt", "w")
# f.write(str(ben2))
# f.close()

# f = open("bengali.txt", "w")
# f.write(str(bengali))
# f.close()
