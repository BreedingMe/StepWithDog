from api import post, post_list, recommend_list

from conf import mongo

from flask import Flask, render_template

from pymongo import MongoClient

# MongoDB 연결
mongo_client = MongoClient('mongodb://' + mongo.config['host'] + '/' + mongo.config['db'], mongo.config['port'])

# Flask 애플리케이션 생성
app = Flask(__name__)
app.db = mongo_client.stepwithdog  # Flask 애플리케이션에 데이터베이스 연결 정보 저장

# Flask Blueprint 연결
app.register_blueprint(post.bp)
app.register_blueprint(post_list.bp)
app.register_blueprint(recommend_list.bp)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=8000, debug=True)
