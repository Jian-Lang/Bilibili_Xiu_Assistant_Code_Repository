# encoding:utf-8
from exits import db


class Xiu_following(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    username = db.Column(db.String(15), nullable = False)
    following_UID = db.Column(db.String(20), nullable = False)
