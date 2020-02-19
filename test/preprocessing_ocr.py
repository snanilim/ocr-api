from PIL import Image 
import pytesseract 
import sys 
from pdf2image import convert_from_path 
import os
import cv2
from matplotlib import pyplot as plt


filename = "/home/nilim/Documents/programmer/ocr-api/test/page_1.jpg"

img = cv2.imread(filename)

img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

img = cv2.blur(img,(5,5))

img = cv2.GaussianBlur(img, (5, 5), 0)

# plt.imshow(img,'gray')
# plt.show()

# cv2.imshow('image', img)
# cv2.waitKey()