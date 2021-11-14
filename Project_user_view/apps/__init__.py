# encoding:utf-8
from flask import Flask

from apps.user.view import user_bp
from exits import db, api
from settings import DevelopmentConfig


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    db.init_app(app = app)
    api.init_app(app = app)
    app.register_blueprint(user_bp)
    return app
