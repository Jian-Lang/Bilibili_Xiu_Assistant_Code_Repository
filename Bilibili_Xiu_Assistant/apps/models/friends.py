# encoding:utf-8
from exits import db


class Friends(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    username = db.Column(db.String(15), nullable = False)
    friend_name = db.Column(db.String(20), nullable = False)
