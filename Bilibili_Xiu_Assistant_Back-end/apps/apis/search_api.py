# encoding:utf-8
from flask import Blueprint
from flask_restful import Resource, reqparse, Api

from apps.models.following_up import Xiu_following
from exits.getsearchresult import getsearchresult

information_bp = Blueprint('search', __name__)
api = Api(information_bp)
search_parser = reqparse.RequestParser()
search_parser.add_argument('content', type = str, required = True)
search_parser.add_argument('username', type = str, required = True)


class SearchApi(Resource):
    def get(self):
        args = search_parser.parse_args()
        username = args.get('username')
        content = args.get('content')
        users = Xiu_following.query.filter(Xiu_following.username == username).all()
        uid_list = []
        if users:
            for user in users:
                uid_list.append(int(user.following_UID))
        return getsearchresult(uid_list, 1, content)


api.add_resource(SearchApi, '/search')
