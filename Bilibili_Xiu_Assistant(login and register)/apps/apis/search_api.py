# encoding:utf-8

from flask import Blueprint
from flask_restful import Resource, reqparse, Api

from exits.Bilibili_method import getsearchresult

information_bp = Blueprint('search', __name__)
api = Api(information_bp)
search_parser = reqparse.RequestParser()
search_parser.add_argument('content', type = str, required = True, help = '请输入内容后搜索')


class SearchApi(Resource):
    def get(self):
        args = search_parser.parse_args()
        content = args.get('content')
        return getsearchresult(content)


api.add_resource(SearchApi, '/search')
