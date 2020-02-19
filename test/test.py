import os
from PIL import Image 
import pytesseract 
import sys 
from pdf2image import convert_from_path 
import os
import cv2
from pathlib import Path

path = '/home/nilim/Documents/SoftExpo2020'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.pdf' in file:
            files.append(os.path.join(r, file))

for path in files:
    print(path)
    base_path = '/home/nilim/Documents'
    text_path = 'SoftExpo2020Text'
    img_path = 'SoftExpo2020Img'

    split_value = path.split('/')
    sector = split_value[5]
    company_name = split_value[6]
    file_name = split_value[7].split('.')
    file_raw_name = file_name[0]

    print(file_raw_name)



    PDF_file = path

    pages = convert_from_path(PDF_file, 500)

    image_counter = 1

    for page in pages:
        filename = f"{base_path}/{img_path}/{sector}/{company_name}/{file_raw_name}_{str(image_counter)}.jpg"
        page.save(filename, 'JPEG')

        # image_counter = image_counter + 1
        # continue

        image = cv2.imread(filename)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

        gray = cv2.medianBlur(gray, 3)

        # page.save(gray, 'JPEG')
        cv2.imwrite(filename, gray)
        image_counter = image_counter + 1

    filelimit = image_counter-1



    for i in range(1, filelimit + 1):
        filename = f"{base_path}/{img_path}/{sector}/{company_name}/{file_raw_name}_{str(i)}.jpg"
        text = str(((pytesseract.image_to_string(Image.open(filename)))))
        text = text.replace('-\n', '')

        outfile = f"{base_path}/{text_path}/{sector}/{company_name}/"
        p = Path(outfile)
        p.mkdir(parents=True, exist_ok=True)
        fn = f"{file_raw_name}_{str(i)}.txt"
        filepath = p / fn
        with filepath.open("w", encoding ="utf-8") as f:
            f.write(text)
        # f = open(outfile, "w")

        # f.write(text)
        f.close()
