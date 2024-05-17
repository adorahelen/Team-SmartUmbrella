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

@app.route('/register')
def register():
    return render_template('register.html')

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

try:
    with conn.cursor() as cursor:
        # 간단한 SELECT 쿼리 실행
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        print("Database connection is successful!" if result else "Database connection failed!")
finally:
    # 연결 종료
    conn.close()



if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=3000)
