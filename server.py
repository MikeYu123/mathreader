import base64
from flask import Flask, request, jsonify
from mathreader.api import *
import os

app = Flask(__name__)

port = os.environ.get('PORT')
port = 5050 if port is None else port

@app.route('/parse', methods=['POST'])
def image_parser():
    input = request.data
    hme_recognizer = HME_Recognizer()
    hme_recognizer.load_image(input, data_type='base64')
    expression, img = hme_recognizer.recognize()
    return jsonify(status='ok', expression=expression)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=port)
