# encoding:utf-8
from flask import Blueprint
from flask_restful import reqparse, Api, Resource

from apps.models.following_up import Xiu_following
from apps.models.user_model import User
from exits import db
from exits.Method_check_myself import check_myself
from exits.Method_get_concerns_information import get_concerns_information
from exits.Method_get_updated_message import get_updated_message

following_bp = Blueprint('following', __name__)
api = Api(following_bp)

add_following_parse = reqparse.RequestParser()
add_following_parse.add_argument('username', type = str, required = True)
add_following_parse.add_argument('uid', type = str, required = True)


class Add_following(Resource):
    def get(self):
        args = add_following_parse.parse_args()
        username = args.get('username')
        uid = args.get('uid')
        add_followings = Xiu_following().query.filter(Xiu_following.username == username).all()
        for add_following in add_followings:
            if add_following.following_UID == uid:
                return {
                    'status': 500,
                    'message': '该用户已关注'
                }
        Up_following = Xiu_following()
        Up_following.username = username
        Up_following.following_UID = uid
        db.session.add(Up_following)
        db.session.commit()
        return {
            'status': 200,
            'message': "添加关注成功"
        }


delete_following_parse = reqparse.RequestParser()
delete_following_parse.add_argument('username', type = str, required = True)
delete_following_parse.add_argument('uid', type = str, required = True)


class Delete_following(Resource):
    def get(self):
        args = delete_following_parse.parse_args()
        username = args.get('username')
        uid = args.get('uid')
        delete_followings = Xiu_following().query.filter(Xiu_following.username == username).all()
        for delete_following in delete_followings:
            if delete_following.following_UID == uid:
                db.session.delete(delete_following)
                db.session.commit()
                return {
                    'status': 200,
                    'message': '取消关注成功'
                }


show_following_parse = reqparse.RequestParser()
show_following_parse.add_argument('username', type = str, required = True)


class Show_following(Resource):
    def get(self):
        args = show_following_parse.parse_args()
        username = args.get('username')
        users = Xiu_following.query.filter(Xiu_following.username == username).all()
        uid_list = []
        if users:
            for user in users:
                uid_list.append(int(user.following_UID))
        return get_concerns_information(uid_list)


show_Bfollowing_parse = reqparse.RequestParser()
show_Bfollowing_parse.add_argument('username', type = str, required = True)


class Show_Bfollowing(Resource):
    def get(self):
        args = show_Bfollowing_parse.parse_args()
        username = args.get('username')
        use = User.query.filter(User.username == username).first()
        users = Xiu_following.query.filter(Xiu_following.username == username).all()
        uid_list = []
        if users:
            for user in users:
                uid_list.append(int(user.following_UID))
        return check_myself(uid_list, use.B_UID)


get_bvideo_parse = reqparse.RequestParser()
get_bvideo_parse.add_argument('username', type = str, required = True)


class Get_bvideo(Resource):
    def get(self):
        args = get_bvideo_parse.parse_args()
        username = args.get('username')
        use = User.query.filter(User.username == username).first()
        users = Xiu_following.query.filter(Xiu_following.username == username).all()
        uid_list = []
        if users:
            for user in users:
                uid_list.append(int(user.following_UID))
        else:
            return {
                'status': 400,
                'message': '该用户还未添加特别关心'
            }
        return get_updated_message(uid_list, use.Day)


api.add_resource(Add_following, '/addfollowing')
api.add_resource(Delete_following, '/deletefollowing')
api.add_resource(Show_following, '/showfollowing')
api.add_resource(Show_Bfollowing, '/showBfollowing')
api.add_resource(Get_bvideo, '/getbvideo')
