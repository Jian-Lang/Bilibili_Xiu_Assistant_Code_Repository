# encoding:utf-8
from exits import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    username = db.Column(db.String(15), nullable = False)
    password = db.Column(db.String(12), nullable = False)
    B_UID = db.Column(db.String(20), nullable = False)
    Sign = db.Column(db.String(255))
    Day = db.Column(db.Integer)

    def __str__(self):
        return self.username
