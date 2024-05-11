from flask import request, jsonify
from .models import db, User
from . import app

# 이후에 app 객체를 사용하는 코드 작성

# 회원가입 엔드포인트
@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    password = data.get('password')

    # 각 필드를 검증하는 로직을 추가할 수 있습니다.

    # 데이터베이스에 새로운 사용자 추가
    new_user = User(first_name=first_name, last_name=last_name, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'Sign up successful'})

# 로그인 엔드포인트
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # 여기에서 로그인 처리 로직을 작성
    # 예를 들어, 데이터베이스에서 이메일과 패스워드를 확인하고 성공 여부를 반환

    # 간단한 예시: 입력한 이메일과 패스워드가 데이터베이스에 있는지 확인
    user = User.query.filter_by(email=email, password=password).first()
    if user:
        return jsonify({'message': 'Login successful'})
    else:
        return jsonify({'message': 'Login failed'}), 401  # 실패시 401 Unauthorized 반환
