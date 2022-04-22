import os

# 환경변수에서 MongoDB 연결 정보 읽기
config = {
    'host': os.getenv('MONGODB_HOST', 'localhost'),
    'port': int(os.getenv('MONGODB_PORT', '27017')),
    'db': 'stepwithdog'
}

# 환경변수에 MongoDB 사용자 정보가 있으면 설정
if os.getenv('MONGODB_USER') != None and os.getenv('MONGODB_PASSWORD') != None:
    config['host'] = os.getenv('MONGODB_USER') + ':' + os.getenv('MONGODB_PASSWORD') + '@' + config['host']
