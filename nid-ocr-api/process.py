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

def imageToOcr(filename, threshold, medianBlur, blurRatio, ocr_model):
    try:
        image = cv2.imread(filename)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        if threshold == 1:
            gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        if medianBlur == 1:
            # print(blurRatio%2)
            if blurRatio > 0 and blurRatio%2 != 0:
                gray = cv2.medianBlur(gray, blurRatio)

        filename = 'process_image/image.jpg'
        cv2.imwrite(filename, gray)

        return_obj = {}
        if "ben" in ocr_model:
            ben = pytesseract.image_to_string(Image.open(filename), lang='ben')
            ben_strings = ben.splitlines()
            return_obj['ben'] = [x.strip() for x in ben_strings if x.strip()]

        if "bengali" in ocr_model:  
            bengali = pytesseract.image_to_string(Image.open(filename), lang='Bengali')
            bengali_strings = bengali.splitlines()
            return_obj['bengali'] = [x.strip() for x in bengali_strings if x.strip()]

        return return_obj
    except Exception as error:
        print('error', error)