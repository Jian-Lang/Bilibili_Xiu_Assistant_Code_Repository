# encoding:utf-8
from flask import Flask

from apps.apis.news_api import news_bp
from apps.apis.user_api import user_bp
from exits import db, cors
from setting import DevelopmentConfig


def create_app():
    app = Flask(__name__, static_folder = '../static')
    app.config.from_object(DevelopmentConfig)
    db.init_app(app = app)
    cors.init_app(app = app, supports_credentials = True)  # ---->跨越处理
    # 注册蓝图
    app.register_blueprint(news_bp)
    app.register_blueprint(user_bp)
    # print(app.url_map)
    return app
