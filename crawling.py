# 크롤링

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
from conf import mongo

# Step with Dog의 DB
mongo_client = MongoClient('mongodb://' + mongo.config['host'] + '/' + mongo.config['db'], mongo.config['port'])
db = mongo_client.stepwithdog

url = 'https://animal.seoul.go.kr/animalplay'

# 해당 url 크롤링
def insert_recommend(url):
    # 타겟 URL을 읽어서 HTML를 받아오고,
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url, headers=headers, verify=False)

    # HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
    # soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
    soup = BeautifulSoup(data.text, 'html.parser')

    trs = soup.select('#mapskip > table > tbody > tr')

    for tr in trs:
        park_name = tr.select_one('td.title').text.strip()
        park_address = tr.select_one('td:nth-child(3)').text
        park_tel = tr.select_one('td:nth-child(5)').text

        # 크롤링한 결과를 딕셔너리로 만듦
        doc = {
            'park_name': park_name,
            'park_address': park_address,
            'park_tel': park_tel
        }

        # 크롤링한 결과(딕셔너리)를 DB에 저장
        db.recommend.insert_one(doc)


# 크롤링 시작
insert_recommend(url)



# 크롤링할 데이터
# mapskip > table > tbody > tr:nth-child(1)
# mapskip > table > tbody > tr

# 공원 이름
# mapskip > table > tbody > tr:nth-child(1) > td.title

# 주소
# mapskip > table > tbody > tr:nth-child(1) > td:nth-child(3)

# 전화번호
# mapskip > table > tbody > tr:nth-child(1) > td:nth-child(5)
