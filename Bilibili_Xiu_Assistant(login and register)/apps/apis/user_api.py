# encoding:utf-8
import os.path

from flask import Blueprint
from flask_restful import Resource, fields, reqparse, Api, marshal_with
from werkzeug.datastructures import FileStorage

from apps.models.user_model import User
from exits import db
from exits.Bilibili_method import judgeuserhasconcern
from settings import Config

# 订制格式 其中的名字必须匹配 名字必须与数据库中的model中的一样
user_bp = Blueprint('user', __name__)
api = Api(user_bp)

# 参数解析
# request.form.get() | request.args.get() | request.cookies.get()
register_parser = reqparse.RequestParser()
register_parser.add_argument('username', type = str, required = True, help = '必须输入用户名',
                             location = ['form'])  # ->required 表示必须填入用户信息，如果没有会返回help中的信息,location限制为post请求，表单提交
register_parser.add_argument('password', type = str, required = True, help = '必须输入密码', location = ['form'])
register_parser.add_argument('B_UID', type = str, required = True, help = '必须输入BILIBILI平台UID', location = ['form'])


class RegisterApi(Resource):  # ----->类视图
    def post(self):
        args = register_parser.parse_args()  # --->获取数据
        username = args.get('username')
        password = args.get('password')
        B_UID = args.get('B_UID')
        name = User.query.filter(User.username == username).first()
        if name is not None:
            return {
                'status': 400,
                'message': '用户名已存在'
            }
        if judgeuserhasconcern(B_UID) is False:
            return {
                'status': 400,
                'message': 'UID异常'
            }
        user = User()
        user.username = username
        user.password = password
        user.B_UID = B_UID
        user.Sign = '该用户什么都没留下哦'
        db.session.add(user)
        db.session.commit()
        return {
            'status': 200,
            'message': '注册成功'
        }


pic_parser = reqparse.RequestParser()
pic_parser.add_argument('icon', type = FileStorage, location = ['files'])
pic_parser.add_argument('username', type = str, required = True, help = '必须输入用户名', location = ['form'])


class UploadPicApi(Resource):
    def post(self):
        args = pic_parser.parse_args()
        username = args.get('username')
        icon = args.get('icon')
        if icon:
            upload_path = os.path.join(Config.UPLOAD_ICON_DIR, username)
            icon.save(upload_path)


login_parser = reqparse.RequestParser()
login_parser.add_argument('username', type = str, required = True, help = '必须输入用户名',
                          location = ['form'])  # ->required 表示必须填入用户信息，如果没有会返回help中的信息,location限制为post请求，表单提交
login_parser.add_argument('password', type = str, required = True, help = '必须输入密码', location = ['form'])


class LoginApi(Resource):
    def post(self):
        args = login_parser.parse_args()
        username = args.get('username')
        password = args.get('password')
        check_name = User.query.filter(User.username == username).first()
        if check_name is None:
            return {
                'status': 400,
                'message': '用户名不存在'
            }
        if check_name.password == password:
            return {
                'status': 200,
                'message': '登录成功'
            }
        else:
            return {
                'status': 400,
                'message': '密码错误'
            }


user_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'B_UID': fields.String,
    'Sign': fields.String
}
getuser_parser = reqparse.RequestParser()
getuser_parser.add_argument('username', type = str, required = True)


class Get_user(Resource):
    @marshal_with(user_fields)
    def get(self):
        args = getuser_parser.parse_args()
        username = args.get('username')
        user = User.query.filter(User.username == username).first()
        return user


api.add_resource(RegisterApi, '/register')
api.add_resource(UploadPicApi, '/upload')
api.add_resource(LoginApi, '/login')
api.add_resource(Get_user, '/getuser')
