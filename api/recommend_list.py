from flask import Blueprint, current_app, jsonify

bp = Blueprint('recommend-list', __name__, url_prefix='/recommend-list')


@bp.route('', methods=['GET'])
def read_recommend_list():
    # 데이터베이스에서 추천 목록 읽기
    recommend_list = list(current_app.db.recommend.find({}, {'_id': False}))

    return jsonify({
        'status': 'success',
        'data': recommend_list
    })
