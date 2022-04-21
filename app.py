from api import post_post, post_get, recommend_list

from conf import mongo

from flask import Flask, render_template

from pymongo import MongoClient

mongo_client = MongoClient('mongodb://' + mongo.config['host'] + '/' + mongo.config['db'], mongo.config['port'])

app = Flask(__name__)
app.db = mongo_client.stepwithdog

app.register_blueprint(post_post.bp)
app.register_blueprint(recommend_list.bp)
app.register_blueprint(post_get.bp)


@app.route('/index')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=8000, debug=True)
