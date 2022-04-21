from flask import Blueprint, current_app, jsonify, request

bp = Blueprint('get', __name__, url_prefix='/')


# /recommend-list로 요청이 들어오면 DB에서 recommend의 데이터를 가져와 클라이언트로 보내줌
@bp.route('/recommend-list', methods=['GET'])
def get_recommend():
    # 크롤링한 데이터를 DB에서 가져온다
    recommend_list = list(current_app.db.recommend.find({}, {'_id': False}))

    # 가져온 데이터를 클라이언트에 보내준다
    return jsonify({'recommend_list': recommend_list})
