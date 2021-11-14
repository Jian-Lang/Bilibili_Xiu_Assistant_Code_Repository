# encoding:utf-8
import datetime

from exits import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    username = db.Column(db.String(15), nullable = False)
    password = db.Column(db.String(12), nullable = False)
    B_UID = db.Column(db.String(11), nullable = False)
    icon = db.Column(db.String(150))
    udatetime = db.Column(db.DateTime, default = datetime.datetime.now)
    #friends = db.relationship('friend', backref = 'user')

    def __str__(self):
        return self.username


class Friend(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    uid = db.Column(db.Integer, db.ForeignKey('user.id'))
    fid = db.Column(db.Integer, db.ForeignKey('user.id'))
