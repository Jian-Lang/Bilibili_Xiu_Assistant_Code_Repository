# encoding:utf-8
from flask import Flask

from apps.apis.following_api import following_bp
from apps.apis.friend_api import friend_bp
from apps.apis.search_api import information_bp
from apps.apis.user_api import user_bp
from exits import db, cors
from settings import DevelopmentConfig


def create_app():
    app = Flask(__name__, static_folder = '../static')
    app.config.from_object(DevelopmentConfig)
    db.init_app(app = app)
    cors.init_app(app = app, supports_credentials = True)  # ---->跨越处理
    # 注册蓝图
    app.register_blueprint(user_bp)
    app.register_blueprint(information_bp)
    app.register_blueprint(friend_bp)
    app.register_blueprint(following_bp)
    return app