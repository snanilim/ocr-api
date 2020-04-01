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

        # if medianBlur == 1:
        #     # print(blurRatio%2)
        #     if blurRatio > 0 and blurRatio%2 != 0:
        #         gray = cv2.medianBlur(gray, blurRatio)
        # if threshold == 1:
        #     gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

        gray = cv2.medianBlur(gray, blurRatio)
        gray = cv2.GaussianBlur(gray, (1, 1), 0)
        # gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 139, 25.0)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
        gray = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

        # gray = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 139, 25.0)
        


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



def preImgToOcr(filename, threshold, medianBlur, blurRatio, ocr_model):
    try:
        img = cv2.imread(filename)
        img = cv2.bilateralFilter(img, 9, 31, 31)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        gray = cv2.medianBlur(gray, 1)
        gray = cv2.GaussianBlur(gray, (1, 1), 0)
        thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 139, 25.0)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
        gray = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

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



def onlyeng(filename, threshold, medianBlur, blurRatio, ocr_model):
    try:
        image = cv2.imread(filename)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # if medianBlur == 1:
        #     # print(blurRatio%2)
        #     if blurRatio > 0 and blurRatio%2 != 0:
        #         gray = cv2.medianBlur(gray, blurRatio)
        # if threshold == 1:
        #     gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

        gray = cv2.medianBlur(gray, blurRatio)
        gray = cv2.GaussianBlur(gray, (1, 1), 0)
        # gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 139, 25.0)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
        gray = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

        # gray = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 139, 25.0)
        


        filename = 'process_image/image.jpg'
        cv2.imwrite(filename, gray)

        return_obj = {}
        if "ben" in ocr_model:
            ben = pytesseract.image_to_string(Image.open(filename))
            ben_strings = ben.splitlines()
            return_obj['eng'] = [x.strip() for x in ben_strings if x.strip()]

        # if "bengali" in ocr_model:  
        #     bengali = pytesseract.image_to_string(Image.open(filename), lang='Bengali')
        #     bengali_strings = bengali.splitlines()
        #     return_obj['bengali'] = [x.strip() for x in bengali_strings if x.strip()]

        return return_obj
    except Exception as error:
        print('error', error)

def test_all_file():
    path = '/home/nilim/Downloads/NID_Front_Image'
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            files.append(os.path.join(r, file))

    for filename in files:
        # result = preImgToOcr(filename, 1, 1, 1, ['ben', 'bengali'])
        result = imageToOcr(filename, 1, 1, 1, ['ben', 'bengali'])
        result['name'] = filename

        print('result', result)
        f = open("eng.txt", "a")
        f.write(str(result) + '\n')
        f.close()


test_all_file()

# 01847418952


# 01911780554_4.png
# 01911780554_3.jpg