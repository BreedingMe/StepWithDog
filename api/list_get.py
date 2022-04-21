from flask import Blueprint, current_app, jsonify, request

bp = Blueprint('get_list', __name__, url_prefix='/post-list')


# /list_get으로 요청이 들어오면 DB에서 recommend의 데이터를 가져와 클라이언트로 보내줌
@bp.route('', methods=['GET'])
def get_list():
    # 크롤링한 데이터를 DB에서 가져온다
    post_list = list(current_app.db.posts.find({}, {'_id': False, 'address': False, 'content': False, 'image': False}))

    # 가져온 데이터를 클라이언트에 보내준다
    return jsonify({'all_list': post_list})
