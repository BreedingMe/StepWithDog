from PIL import Image

import base64
import cv2
import io
import numpy as np


def convert_ndarray_to_base64(array):
    return base64.b64encode(array).decode('utf-8')  # NumPy 배열을 BASE64로 인코딩


def convert_img_file_to_ndarray(img_file):
    # 이미지 파일 읽기
    image = img_file.read()
    image = Image.open(io.BytesIO(image))

    # RGB 형식이 아니면 RGB 형식으로 변경
    if image.mode != 'RGB':
        image = image.convert('RGB')

    # 이미지 파일을 NumPy 배열로 변환
    image = np.asarray(image)
    image = image.astype(np.uint8)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    return image
