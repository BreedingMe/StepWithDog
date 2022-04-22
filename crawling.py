from bs4 import BeautifulSoup

from conf import mongo

from pymongo import MongoClient

import requests

# MongoDB 연결
mongo_client = MongoClient('mongodb://' + mongo.config['host'] + '/' + mongo.config['db'], mongo.config['port'])
db = mongo_client.stepwithdog


def insert_recommend_list(url):
    # HTTP 헤더 설정
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    }

    # HTML 데이터 획득
    data = requests.get(url, headers=headers, verify=False)

    # HTML 데이터 파싱
    soup = BeautifulSoup(data.text, 'html.parser')

    # 파싱한 데이터 분석
    parks = soup.select('#mapskip > table > tbody > tr')

    for park in parks:
        park_name = park.select_one('td.title').text.strip()
        park_address = park.select_one('td:nth-child(3)').text
        park_tel = park.select_one('td:nth-child(5)').text

        doc = {
            'park_name': park_name,
            'park_address': park_address,
            'park_tel': park_tel
        }

        # 데이터베이스에 공원 정보 삽입
        db.recommend.insert_one(doc)


def delete_recommend_list():
    # 데이터베이스 초기화
    db.recommend.delete_many({})


if __name__ == '__main__':
    delete_recommend_list()
    insert_recommend_list('https://animal.seoul.go.kr/animalplay')
