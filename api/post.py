from bson.objectid import ObjectId

from flask import Blueprint, current_app, jsonify, request

from utils.image import convert_img_file_to_ndarray, convert_ndarray_to_base64

import cv2

# Flask Blueprint 생성
bp = Blueprint('post', __name__, url_prefix='/post')


@bp.route('/<post_id>', methods=['GET'])
def read_post(post_id):
    # 데이터베이스에서 게시글 읽기
    post = current_app.db.posts.find_one({'_id': ObjectId(post_id)}, {'_id': False})

    return jsonify({
        'status': 'success',
        'data': post
    })


@bp.route('', methods=['POST'])
def write_post():
    # Request 파라미터를 딕셔너리로 변환
    data = request.form.to_dict()

    # 제목, 내용, 주소 파라미터
    title = data['title']
    content = data['content']
    address = data['address']

    # 이미지 파라미터
    image = request.files['image']
    image = convert_img_file_to_ndarray(image)  # 이미지 파일을 NumPy 배열로 변경
    thumbnail = cv2.resize(image, dsize=(640, 480), interpolation=cv2.INTER_AREA)  # 이미지 리사이즈해서 썸네일 생성

    # 이미지를 PNG 포맷으로 인코딩
    _, image = cv2.imencode('.png', image)
    _, thumbnail = cv2.imencode('.png', thumbnail)

    # 이미지를 BASE64 포맷으로 인코딩
    image = 'data:image/png;base64,' + convert_ndarray_to_base64(image)
    thumbnail = 'data:image/png;base64,' + convert_ndarray_to_base64(thumbnail)

    doc = {
        'title': title,
        'content': content,
        'address': address,
        'image': image,
        'thumbnail': thumbnail
    }

    # 데이터베이스 게시글 삽입
    current_app.db.posts.insert_one(doc)

    return jsonify({
        'status': 'success'
    })
