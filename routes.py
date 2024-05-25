from flask import Blueprint, request, jsonify, send_from_directory
from models import db, User
from werkzeug.security import generate_password_hash, check_password_hash  # 추가

main = Blueprint('main', __name__, static_url_path='', static_folder='build')

@main.route('/')
def index():
    return send_from_directory('build', 'index.html')

@main.route('/login')
def login_page():
    return send_from_directory('build', 'index.html')

@main.route('/signup')
def signup_page():
    return send_from_directory('build', 'index.html')

@main.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()

    first_name = data.get('firstName')
    last_name = data.get('lastName')
    email = data.get('email')
    password = data.get('password')

    # # 비밀번호 해시화
    # hashed_password = generate_password_hash(password, method='sha256')

    # 새 사용자 생성 및 데이터베이스에 추가
    new_user = User(first_name=first_name, last_name=last_name, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()

    print(f"Received signup data: {data}")

    # 회원가입 성공 응답
    response = {
        'message': 'User registered successfully',
        'user': {
            'firstName': first_name,
            'lastName': last_name,
            'email': email,
        }
    }

    return jsonify(response), 201
