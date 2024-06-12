from flask import Flask
from config import Config
from models import db
from routes import main

app = Flask(__name__, static_url_path='', static_folder='build')
app.config.from_object(Config)

# SQLAlchemy 초기화
db.init_app(app)

# Blueprint 등록
app.register_blueprint(main)

# 데이터베이스 초기화
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True, host='10.32.40.121', port=3000)
    #주기적인 IP 수정 필요, CMD => IP confih => host부분 수정
    #if 로컬 네트워크 통신, 같은 네트워크 잡아야 함
