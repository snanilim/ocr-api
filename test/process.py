import os
from PIL import Image 
import pytesseract 
import sys 
from pdf2image import convert_from_path 
import os
import cv2
from pathlib import Path

# /usr/local/Cellar/tesseract/4.0.0_1/bin/tesseract [for mac]
# /usr/share/tesseract-ocr/4.00/tessdata [for linux]

def imageToOcr(filename):
    try:
        # filename = '/home/nilim/Documents/programmer/ocr-api/test/nid03.jpg'
        image = cv2.imread(filename)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

        gray = cv2.medianBlur(gray, 1)

        # # page.save(gray, 'JPEG')
        filename = 'process_image/image.jpg'
        cv2.imwrite(filename, gray)

        # # ben = pytesseract.image_to_string(Image.open(file_name))
        # ben = pytesseract.image_to_string(Image.open(filename))
        # ben2 = pytesseract.image_to_string(Image.open(filename2), lang='ben')

        ben = pytesseract.image_to_string(Image.open(filename), lang='ben')
        ben2 = pytesseract.image_to_string(Image.open(filename), lang='ben2')
        bengali = pytesseract.image_to_string(Image.open(filename), lang='Bengali')

        # print(ben)

        # f = open("result/ben.txt", "w")
        # f.write(str(ben))
        # f.close()

        # f = open("result/ben2.txt", "w")
        # f.write(str(ben2))
        # f.close()

        # f = open("result/bengali.txt", "w")
        # f.write(str(bengali))
        # f.close()

        return {"ben": ben, "bengali": bengali}
    except Exception as error:
        print('error', error)