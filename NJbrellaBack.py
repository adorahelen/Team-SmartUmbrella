from flask import Flask, send_from_directory, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import json
from models import db, User
from flask import Flask, request, jsonify

app = Flask(__name__, static_url_path='', static_folder='build')

# SQLAlchemy 초기화
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


# 기본 라우트
@app.route('/')
def index():
    return send_from_directory('build', 'index.html')


@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    # 여기서는 간단히 이메일과 패스워드를 출력하는 예시입니다.
    print(f"Received email: {email}, password: {password}")

    # 로그인 성공 여부에 따라 응답을 반환할 수도 있습니다.
    # 여기서는 간단히 성공 메시지를 반환합니다.
    return jsonify({"message": "Login successful!"})


@app.route('/signup', methods=['POST'])
def signup():
    # POST 요청에서 데이터 추출
    data = request.json

    # 데이터 출력
    print(data)

    # 여기서는 간단히 성공 메시지를 반환
    return jsonify({"message": "Signup successful!"})


if __name__ == '__main__':
    app.run(debug=True, host='10.32.40.139', port=3000)
