from flask import Blueprint, current_app, jsonify, request

bp = Blueprint('post', __name__, url_prefix='/post')


@bp.route('', methods=['POST'])
def save_post():
    data = request.form.to_dict()

    title = data['title']
    content = data['content']
    address = data['address']

    doc = {
        'title': title,
        'content': content,
        'address': address
    }

    current_app.db.posts.insert_one(doc)

    return jsonify({
        'status': 'success'
    })
