from flask import Blueprint, current_app, jsonify

bp = Blueprint('post-list', __name__, url_prefix='/post-list')


@bp.route('', methods=['GET'])
def read_post_list():
    # 데이터베이스에서 게시글 목록을 읽어와서 최신순으로 정렬
    post_list = list(
        current_app.db.posts.find({}, {'address': False, 'content': False, 'image': False}).sort('_id', -1))

    # _id 열을 문자열 포맷으로 변환
    for index in range(len(post_list)):
        post_list[index]['_id'] = str(post_list[index]['_id'])

    return jsonify({
        'status': 'success',
        'data': post_list
    })
