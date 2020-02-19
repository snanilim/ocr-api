import os
from flask import Flask, request, jsonify
from datetime import datetime
from process import imageToOcr
from PIL import Image
from io import BytesIO
import re, time, base64
import numpy as np
import cv2

app = Flask(__name__, static_url_path='', static_folder='./',)


# file formate check
def file_formate_check(filename):
    if filename.endswith("png") or filename.endswith("jpg") or filename.endswith("jpeg"):
        return True
    else:
        return False


def data_uri_to_cv2_img(uri):
    encoded_data = uri.split(',')[1]
    nparr = np.fromstring(base64.b64decode(encoded_data), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img


@app.route('/')
def index():
    return jsonify({"message": "API Start"})


@app.route('/upload-image', methods=['GET', 'POST'])
def uploadNid():
    if request.method == 'GET':
        return jsonify({"result": "Its A post request Please use a 'POST' method"})

    if request.method == 'POST':
        print('body', type(request.data))
        # print('body', request.get_json()['nid_number'])
        threshold = request.get_json()['threshold']
        medianBlur = request.get_json()['medianBlur']
        blurRatio = request.get_json()['blurRatio']
        ocr_model = request.get_json()['ocr_model']
        base64_image = request.get_json()['img_path']
        img_path = "raw_image/raw_image.jpg"

        image = data_uri_to_cv2_img(base64_image)
        cv2.imwrite(img_path, image)


        result = imageToOcr(img_path, threshold, medianBlur, blurRatio, ocr_model)
        return jsonify({ "result": "Success", "data": result})
        


if __name__ == "__main__":
    app.run(host= 'localhost', port=3000)
