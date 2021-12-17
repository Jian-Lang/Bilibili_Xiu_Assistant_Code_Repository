# encoding:utf-8
from flask import Blueprint
from flask_restful import reqparse, Api, Resource

from apps.models.following_up import Xiu_following
from apps.models.friends import Friends
from apps.models.user_model import User
from exits import db
from exits.Method_check_friend import check_friend
from exits.Method_check_myself import check_myself

friend_bp = Blueprint('friend', __name__)
api = Api(friend_bp)

search_friend_parse = reqparse.RequestParser()
search_friend_parse.add_argument('username', type = str, required = True)
search_friend_parse.add_argument('friendname', type = str, required = True)


class Search_friendApi(Resource):
    def get(self):
        args = search_friend_parse.parse_args()
        username = args.get('username')
        friendname = args.get('friendname')
        users = Friends.query.filter(Friends.username == username)
        for i in users:
            if i.friend_name == friendname:
                user = User.query.filter(User.username == friendname).first()
                return {
                    'status': 200,
                    'username': user.username,
                    'sign': user.Sign,
                    'message': 1
                }
        friend = User.query.filter(User.username == friendname).first()
        if friend is None:
            return {
                'status': 400,
                'message': '小伙伴不存在哦'
            }
        else:
            return {
                'status': 200,
                'username': friend.username,
                'sign': friend.Sign,
                'message': 0
            }


add_friend_parse = reqparse.RequestParser()
add_friend_parse.add_argument('username', type = str, required = True)
add_friend_parse.add_argument('friendname', type = str, required = True)


class Add_friendApi(Resource):
    def get(self):
        args = add_friend_parse.parse_args()
        username = args.get('username')
        friend_name = args.get('friendname')
        friend = Friends()
        friend.friend_name = friend_name
        friend.username = username
        db.session.add(friend)
        db.session.commit()
        return {
            'status': 200,
            'message': "添加好友成功"
        }


get_friend_parse = reqparse.RequestParser()
get_friend_parse.add_argument('username')


class Get_friendApi(Resource):
    def get(self):
        friend_list = []
        args = get_friend_parse.parse_args()
        username = args.get('username')
        User_friend = Friends.query.filter(Friends.username == username).all()
        if User_friend is None:
            return {
                'status': 400,
                'message': '没有好友'
            }
        for friend in User_friend:
            user = User.query.filter(User.username == friend.friend_name).first()
            friend = {
                'username': user.username,
                'Sign': user.Sign,
            }
            friend_list.append(friend)
        return {
            'status': 200,
            'num': len(friend_list),
            'friend_information': friend_list
        }


delete_friend_parse = reqparse.RequestParser()
delete_friend_parse.add_argument('username')
delete_friend_parse.add_argument('friendname')


class Delete_friendApi(Resource):
    def get(self):
        args = delete_friend_parse.parse_args()
        username = args.get('username')
        friendname = args.get('friendname')
        users = Friends.query.filter(Friends.username == username)
        for user in users:
            if user.friend_name == friendname:
                db.session.delete(user)
                db.session.commit()
                return {
                    'status': 200,
                    'message': '删除成功'
                }


friend_concern_parse = reqparse.RequestParser()
friend_concern_parse.add_argument('username')
friend_concern_parse.add_argument('friendname')


class Friend_concern(Resource):
    def get(self):
        args = friend_concern_parse.parse_args()
        username = args.get('username')
        friendname = args.get('friendname')
        users = Xiu_following.query.filter(Xiu_following.username == username).all()
        uid_list = []
        if users:
            for user in users:
                uid_list.append(int(user.following_UID))
        friend_list = []
        friends = Xiu_following.query.filter(Xiu_following.username == friendname).all()
        if friends:
            for friend in friends:
                friend_list.append(int(friend.following_UID))
        else:
            return {
                'status': 400,
                'message': "该用户还没有添加关注呦"
            }
        print(uid_list)
        print(friend_list)
        return check_friend(uid_list, friend_list)


friend_bconcern_parse = reqparse.RequestParser()
friend_bconcern_parse.add_argument('username')
friend_bconcern_parse.add_argument('friendname')


class Friend_Bconcern(Resource):
    def get(self):
        args = friend_bconcern_parse.parse_args()
        username = args.get('username')
        frinedname = args.get('friendname')
        friend = User.query.filter(User.username == frinedname).first()
        users = Xiu_following.query.filter(Xiu_following.username == username).all()
        uid_list = []
        if users:
            for user in users:
                uid_list.append(int(user.following_UID))
        return check_myself(uid_list, friend.B_UID)


api.add_resource(Add_friendApi, '/addfriend')
api.add_resource(Search_friendApi, '/searchfriend')
api.add_resource(Get_friendApi, '/getfriend')
api.add_resource(Delete_friendApi, '/deletefriend')
api.add_resource(Friend_concern, '/showfriendconcern')
api.add_resource(Friend_Bconcern, '/showfriendBconcern')
