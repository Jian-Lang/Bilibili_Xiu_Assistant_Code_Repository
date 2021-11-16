# encoding:utf-8
from apps.models import BaseModel
from exits import db


class User(BaseModel):
    __tablename__ = 'user'
    username = db.Column(db.String(50), nullable = False, unique = False)
    password = db.Column(db.String(128))
    phone = db.Column(db.String(11), unique = True, nullable = False)
    icon = db.Column(db.String(256))
    newsList = db.relationship('News', backref = 'author')

    def __str__(self):
        return self.username
