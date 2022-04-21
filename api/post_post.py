from flask import Blueprint, current_app, jsonify, request

from utils.image import convert_img_file_to_ndarray, convert_ndarray_to_base64

import cv2

bp = Blueprint('post', __name__, url_prefix='/post')


@bp.route('', methods=['POST'])
def save_post():
    data = request.form.to_dict()

    title = data['title']
    content = data['content']
    address = data['address']

    image = request.files['image']
    image = convert_img_file_to_ndarray(image)
    thumbnail = cv2.resize(image, dsize=(640, 480), interpolation=cv2.INTER_AREA)

    _, image = cv2.imencode('.png', image)
    _, thumbnail = cv2.imencode('.png', thumbnail)

    image = 'data:image/png;base64,' + convert_ndarray_to_base64(image)
    thumbnail = 'data:image/png;base64,' + convert_ndarray_to_base64(thumbnail)

    doc = {
        'title': title,
        'content': content,
        'address': address,
        'image': image,
        'thumbnail': thumbnail
    }

    current_app.db.posts.insert_one(doc)

    return jsonify({
        'status': 'success'
    })
