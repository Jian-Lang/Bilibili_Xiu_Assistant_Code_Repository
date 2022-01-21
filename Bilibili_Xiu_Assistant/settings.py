# encoding:utf-8
import os


class Config:
    DEBUG = True
    USERNAME = 'root'
    PASSWORD = 'root'
    HOST = '127.0.0.1'
    PORT = '3306'
    DATABASE = 'project_db'
    DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8' \
        .format(USERNAME, PASSWORD, HOST, PORT, DATABASE)
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    SECRET_KEY = 'JOHNSON'
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    STATIC_DIR = os.path.join(BASE_DIR, 'static')
    UPLOAD_ICON_DIR = os.path.join(STATIC_DIR, 'upload/icon')


class DevelopmentConfig(Config):
    ENV = 'development'


class ProductionConfig(Config):
    ENV = 'production'
    DEBUG = False
