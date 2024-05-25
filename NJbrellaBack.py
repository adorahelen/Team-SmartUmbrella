# import os
# import pymysql
# from flask import Flask, send_from_directory, request, jsonify, render_template
# from models import db, User
# from flask_sqlalchemy import SQLAlchemy
# from werkzeug.security import generate_password_hash, check_password_hash
#
#
# # 데이터베이스에 연결
# conn = pymysql.connect(
#     host='127.0.0.1',
#     user='root',
#     password='0000',
#     db='njdb',
#     charset='utf8'
# )
#
# app = Flask(__name__, static_url_path='', static_folder='build')
#
# # SQLAlchemy 초기화
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# db.init_app(app)
#
# # 기본 라우트
# @app.route('/')
# def index():
#     return send_from_directory('build', 'index.html')
# @app.route('/login')
# def login():
#     return send_from_directory('build', 'index.html')
# @app.route('/signup')
# def signup():
#     return send_from_directory('build', 'index.html')
#
# # 여기까지는 홈페이지를 제공하는 라우팅 함수
#
#
# @app.route('/signup', methods=['POST'])
# def signup2():
#     data = request.get_json()
#
#     first_name = data.get('firstName')
#     last_name = data.get('lastName')
#     email = data.get('email')
#     password = data.get('password')
#
#     print(f"Received signup data: {data}")
#
#     # 회원가입 성공 응답
#     response = {
#         'message': 'User registered successfully',
#         'user': {
#             'firstName': first_name,
#             'lastName': last_name,
#             'email': email,
#         }
#     }
#
#     return jsonify(response), 201
#
#
# if __name__ == '__main__':
#     app.run(debug=True, host='127.0.0.1', port=3000)
