import os
import pymysql
from flask import Flask, send_from_directory, request, jsonify, render_template
from models import db, User

# 데이터베이스에 연결
conn = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='0000',
    db='njdb',
    charset='utf8'
)

app = Flask(__name__, static_url_path='', static_folder='build')

# SQLAlchemy 초기화
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

# 기본 라우트
@app.route('/')
def index():
    return send_from_directory('build', 'index.html')

@app.route('/login')
def login():
    return send_from_directory('build', 'Login.js')


@app.route('/signup')
def signup():
    # Signup.js 파일을 제공하도록 수정
    return send_from_directory('build', 'Signup.js')


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=3000)
