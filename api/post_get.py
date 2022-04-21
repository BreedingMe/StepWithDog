from flask import Blueprint, current_app, jsonify
from bson.objectid import ObjectId

bp = Blueprint('get', __name__, url_prefix='/post')


@bp.route('/<post_id>', methods=['GET'])
def get_post(post_id):
    post = current_app.db.posts.find_one({'_id': ObjectId(post_id)}, {'_id': False})  # posts로 부터 게시글을 가져와서 post변수에 저장

    return jsonify({  # 저장해놓은 변수를 서버에 반환
        'status': 'success',
        'data': post
    })