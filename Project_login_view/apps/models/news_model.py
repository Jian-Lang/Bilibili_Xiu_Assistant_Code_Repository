# encoding:utf-8
from apps.models import BaseModel
from exits import db


class NewsType(BaseModel):
    __tablename__ = 'news_type'  # ---->继承父类
    type_name = db.Column(db.String(50), nullable = False)


class News(BaseModel):
    __tablename__ = 'news'
    title = db.Column(db.String(100), nullable = False)
    content = db.Column(db.Text, nullable = False)
    new_type_id = db.Column(db.Integer, db.ForeignKey('news_type.id'))
