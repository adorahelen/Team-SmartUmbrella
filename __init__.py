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
    app.run(debug=True, host='127.0.0.1', port=3000)
