import os
from flask import Flask, request, jsonify
from datetime import datetime
from process import imageToOcr, processImgToOcr, base64_to_image
from webScrap import scrapNidSite
from PIL import Image
from io import BytesIO
import re, time, base64
import numpy as np
import cv2

app = Flask(__name__, static_url_path='', static_folder='./',)

@app.route('/')
def index():
    return jsonify({"message": "API Start"})



@app.route('/img-to-ocr', methods=['GET', 'POST'])
def imgToOcr():
    if request.method == 'GET':
        return jsonify({"result": "Its A post request Please use a 'POST' method"})

    if request.method == 'POST':
        try:
            print('body', type(request.data))
            # print('body', request.get_json()['nid_number'])
            threshold = request.get_json()['threshold']
            medianBlur = request.get_json()['medianBlur']
            scale = request.get_json()['scale']
            blurRatio = request.get_json()['blurRatio']
            ocr_model = request.get_json()['ocr_model']
            base64_image = request.get_json()['img_path']
            img_path = "raw_image/raw_image.jpg"

            base64_to_image(base64_image, img_path)


            result = processImgToOcr(img_path, threshold, medianBlur, scale, blurRatio, ocr_model)
            return jsonify({ "result": "Success", "data": result})
        except Exception as error:
            print('imgToOcr', error)
            return jsonify({"is_success": False, "message": "Failed to convert image to ocr. please try again"})



@app.route('/web-scrap', methods=['GET', 'POST'])
def webToScrap():
    if request.method == 'GET':
        return jsonify({"result": "Its A post request Please use a 'POST' method"})

    if request.method == 'POST':
        try:
            print('body', type(request.data))
            # print('body', request.get_json()['nid_number'])
            url = request.get_json()['url']
            nid = request.get_json()['nid']
            dob = request.get_json()['dob']

            print(url, nid, dob)

            result = scrapNidSite(url, nid, dob)
            return jsonify({ "result": "Success", "data": result})
        except Exception as error:
            print('imgToOcr', error)
            return jsonify({"is_success": False, "message": "Failed to web scraping. please try again"})


@app.route('/test-img-to-ocr', methods=['GET', 'POST'])
def testImgToOcr():
    if request.method == 'GET':
        try:
            img_path = "raw_image/test_raw_image.jpg"
            result = processImgToOcr(img_path, 0, 1, 1, 1, ['ben', 'bengali'])
            return jsonify({ "result": "Success", "data": result})
        except Exception as error:
            print('imgToOcr', error)
            return jsonify({"is_success": False, "message": "Failed to convert image to ocr. Please try again"})


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

        base64_to_image(base64_image, img_path)


        result = imageToOcr(img_path, threshold, medianBlur, blurRatio, ocr_model)
        return jsonify({ "result": "Success", "data": result})
        


if __name__ == "__main__":
    app.run(host= '0.0.0.0', port=3000)
