import os

config = {
    'host': os.getenv('MONGODB_HOST', 'localhost'),
    'port': int(os.getenv('MONGODB_PORT', '27017')),
    'db': 'stepwithdog'
}

if os.getenv('MONGODB_USER') != None and os.getenv('MONGODB_PASSWORD') != None:
    config['host'] = os.getenv('MONGODB_USER') + ':' + os.getenv('MONGODB_PASSWORD') + '@' + config['host']
