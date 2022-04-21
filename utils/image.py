from PIL import Image

import base64
import cv2
import io
import numpy as np


def convert_ndarray_to_base64(array):
    return base64.b64encode(array).decode('utf-8')


def convert_img_file_to_ndarray(img_file):
    image = img_file.read()
    image = Image.open(io.BytesIO(image))

    if image.mode != 'RGB':
        image = image.convert('RGB')

    image = np.asarray(image)
    image = image.astype(np.uint8)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    return image
