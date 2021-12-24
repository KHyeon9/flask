import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))  # 데이터 베이스 접속 주소
SQLALCHEMY_TRACK_MODIFICATIONS = False  # SQLAlchemy의 이밴트 처리 옵션

SECRET_KEY = "dev"