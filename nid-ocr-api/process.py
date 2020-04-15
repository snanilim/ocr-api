import os
from PIL import Image 
import pytesseract 
import sys 
# from pdf2image import convert_from_path 
import os
import cv2
from pathlib import Path
import PIL
from PIL import Image, ExifTags, ImageOps
from io import BytesIO
import re, time, base64

# /usr/local/Cellar/tesseract/4.0.0_1/bin/tesseract [for mac]
# /usr/share/tesseract-ocr/4.00/tessdata [for linux]

def rotate_image(im):
    try:
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation]=='Orientation':
                break
        exif=dict(im._getexif().items())
        print('exif[orientation]', exif[orientation])
        if exif[orientation] == 3:
            im=im.rotate(180, expand=True)
        elif exif[orientation] == 6:
            im=im.rotate(270, expand=True)
        elif exif[orientation] == 8:
            im=im.rotate(90, expand=True)

        return im
    except Exception as error:
        print('error_rotate_image', error)
        return False

def resize_image(image):
    try:
        basewidth = 650
        if float(image.size[0]) > basewidth:
            wpercent = (basewidth / float(image.size[0]))
            hsize = int((float(image.size[1]) * float(wpercent)))
            image = image.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
            return image
        else:
            return image
    except Exception as error:
        print('resize_image', error)
        return False


def base64_to_image(base64_image, img_path):
    try:
        # print('base64_image', base64_image)
        encoded_data = base64_image.split(',')[1]
        im = Image.open(BytesIO(base64.b64decode(encoded_data)))
        image = rotate_image(im)
        if image:
            reImg = resize_image(image)
        else:
            reImg = resize_image(im)
        reImg.convert('RGB').save(img_path)

        return True
    except Exception as error:
        print('base64_to_image', error)
        return error


def processImgToOcr(filename, threshold, medianBlur, scale, blurRatio, ocr_model):
    try:
        image = cv2.imread(filename)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        if scale == 1:
            print('scale')
            gray = cv2.resize(gray, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
        if medianBlur == 1:
            gray = cv2.medianBlur(gray, blurRatio)
            gray = cv2.GaussianBlur(gray, (1, 1), 0)
        if threshold == 1:
            thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 139, 25.0)
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
            gray = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

        filename = 'process_image/image.jpg'
        cv2.imwrite(filename, gray)

        return_obj = {}
        if "ben" in ocr_model:
            print('ben----------')
            ben = pytesseract.image_to_string(Image.open(filename), lang='ben')
            ben_strings = ben.splitlines()
            return_obj['ben'] = [x.strip() for x in ben_strings if x.strip()]

        if "bengali" in ocr_model:
            print('bengali----------')
            bengali = pytesseract.image_to_string(Image.open(filename), lang='Bengali')
            bengali_strings = bengali.splitlines()
            return_obj['bengali'] = [x.strip() for x in bengali_strings if x.strip()]

        return return_obj
    except Exception as error:
        print('processImgToOcr', error)
        return error







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
        print('error_imageToOcr', error)
        return error


# def onlyeng(filename, threshold, medianBlur, blurRatio, ocr_model):
#     try:
#         image = cv2.imread(filename)

#         gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#         gray = cv2.medianBlur(gray, blurRatio)
#         gray = cv2.GaussianBlur(gray, (1, 1), 0)
#         # gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
#         thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 139, 25.0)
#         kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
#         gray = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

#         # gray = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 139, 25.0)
        
#         filename = 'process_image/image.jpg'
#         cv2.imwrite(filename, gray)

#         return_obj = {}
#         if "ben" in ocr_model:
#             ben = pytesseract.image_to_string(Image.open(filename))
#             ben_strings = ben.splitlines()
#             return_obj['eng'] = [x.strip() for x in ben_strings if x.strip()]

#         return return_obj
#     except Exception as error:
#         print('error', error)

def test_all_file():
    path = '/home/nilim/Downloads/NID_Front_Image'
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            files.append(os.path.join(r, file))

    for filename in files:
        # result = preImgToOcr(filename, 1, 1, 1, ['ben', 'bengali'])
        result = processImgToOcr(filename, 0, 1, 1, 1, ['ben', 'bengali'])
        result['name'] = filename

        print('result', result)
        f = open("process-02.txt", "a")
        f.write(str(result) + '\n')
        f.close()


if __name__ == "__main__":
    test_all_file()

# def backup():
#     img = cv2.imread(filename)
#     img = cv2.bilateralFilter(img, 9, 31, 31)
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
#     gray = cv2.medianBlur(gray, 1)
#     gray = cv2.GaussianBlur(gray, (1, 1), 0)
#     thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 139, 25.0)
#     kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
#     gray = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)


# gray = cv2.resize(gray, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
# gray = cv2.resize(gray, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
# gray = cv2.resize(gray, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)


# ocr_01.jpg
# 01921011814.png
# 01911780554_3.jpg
# 01921011823.png
# 01848622592.png