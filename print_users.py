import os
from models import db, User, Log  # Log 모델 추가
from config import Config
from flask import Flask
import json

app = Flask(__name__)
app.config.from_object(Config)

# SQLAlchemy 초기화
db.init_app(app)

def print_users():
    with app.app_context():
        users = User.query.all()
        if not users:
            print("No users found in the database.")
            return

        for user in users:
            print(f"First Name: {user.first_name}, Last Name: {user.last_name}, Email: {user.email}, password: {user.password}")

def print_logs():
    with app.app_context():
        logs = Log.query.all()
        if not logs:
            print("No logs found in the database.")
            return

        for log in logs:
            print(f"ID: {log.id}, Data: {json.loads(log.data)}, Timestamp: {log.timestamp}")

if __name__ == '__main__':
    print_logs()
    print_users()
    #이 부분에 추가해야 함수를 사용, 위에 정의된 두 함수는  각각 DB > table에 저장된 data 출력/조회 하는 함수