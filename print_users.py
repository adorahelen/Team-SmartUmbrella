import os
from models import db, User
from config import Config
from flask import Flask

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


if __name__ == '__main__':
    print_users()
