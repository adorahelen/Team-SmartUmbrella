import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:0000@127.0.0.1/njdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
