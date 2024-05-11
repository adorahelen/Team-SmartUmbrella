from flask import Flask, send_from_directory, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import json
from models import db, User

app = Flask(__name__, static_url_path='', static_folder='build')

# SQLAlchemy 초기화
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


# 기본 라우트
@app.route('/')
def index():
    return send_from_directory('build', 'index.html')

if __name__ == '__main__':
    app.run(debug=True, host='10.32.40.139', port=3000)
