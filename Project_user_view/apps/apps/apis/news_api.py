# encoding:utf-8
from flask import Blueprint
from flask_restful import Api, Resource, fields, marshal_with, reqparse

from apps.models.news_model import NewsType

news_bp = Blueprint('news', __name__)
api = Api(news_bp)

types_fields = {
    'id': fields.Integer,
    'name': fields.String(attribute = 'type_name')
}


# 新闻类型
class NewsTypeApi(Resource):
    @marshal_with(types_fields)  # -->按照这个方式格式化输出
    def get(self):
        types = NewsType.query.all()
        return types  # newsType 属于自定义的一个类型 需要数列化为json


news_parser = reqparse.RequestParser()
news_parser.add_argument('type_id', type = int, help = '必须添加新闻类型id', required = True)
news_parser.add_argument('page', type = int)

news_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'desc': fields.String,
    'datatime': fields.DateTime(attribute = 'data_time'),
    'url': fields.Url('news.url', absolute = True)  # -->发出完整路径
}


# 新闻api
# class NewsApi(Resource):
#     # 获取新闻分类下的新闻
#     def get(self):
#         args = news_parser.parse_args()
#         typeid = args.get('typeid')
#         page = args.get('page', 1)
#         # newstype = NewsType.query.get(typeid)
#         pagination = News.query.filter(News.new_type_id == typeid).paginate(page = page, per_page = 8)
#         data = {
#             'has_more': pagination.has_next,
#             'data': pagination.items,
#             'return_count': pagination.page,
#             'html': 'null'
#         }


api.add_resource(NewsTypeApi, '/types')
