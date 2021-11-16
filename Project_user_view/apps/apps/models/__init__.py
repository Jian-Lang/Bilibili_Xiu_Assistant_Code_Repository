# encoding:utf-8
from datetime import datetime

from exits import db


class BaseModel(db.Model):
    __abstract__ = True  # --->作为一个父类出现,永远被使用，不然会被子重名
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    data_time = db.Column(db.DateTime, default = datetime.now)
