from mathreader.api import *

hme_recognizer = HME_Recognizer()

image = 'mathreader/images/validation/10.png'

try:
    # To use with base64 string, use data_type='base64'
    hme_recognizer.load_image(image, data_type='path')
    expression, img = hme_recognizer.recognize()
    print("Latex: ", expression)
except Exception as e:
    print('Exception: ', e)
