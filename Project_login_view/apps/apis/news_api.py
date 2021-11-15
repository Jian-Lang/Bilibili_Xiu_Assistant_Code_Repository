# encoding:utf-8
from flask import Blueprint
from flask_restful import Api, Resource, fields, marshal_with

from apps.models.news_model import NewsType

news_bp = Blueprint('news', __name__)
api = Api(news_bp)

types_fields = {
    'id': fields.Integer,
    'name': fields.String(attribute = 'type_name')
}


class NewsTypeApi(Resource):
    @marshal_with(types_fields)  # -->按照这个方式格式化输出
    def get(self):
        types = NewsType.query.all()
        return types  # newsType 属于自定义的一个类型 需要数列化为json


api.add_resource(NewsTypeApi, '/types')
