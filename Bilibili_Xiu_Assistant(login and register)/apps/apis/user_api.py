# encoding:utf-8
import os.path

from flask import Blueprint
from flask_restful import Resource, fields, reqparse, Api
from werkzeug.datastructures import FileStorage

from apps.models.user_model import User
from exits import db
from settings import Config

# 订制格式 其中的名字必须匹配 名字必须与数据库中的model中的一样
user_bp = Blueprint('user', __name__)
api = Api(user_bp)
user_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'password': fields.String,
    'B_UID': fields.String
}
# 参数解析
# request.form.get() | request.args.get() | request.cookies.get()
register_parser = reqparse.RequestParser()
register_parser.add_argument('username', type = str, required = True, help = '必须输入用户名',
                             location = ['form'])  # ->required 表示必须填入用户信息，如果没有会返回help中的信息,location限制为post请求，表单提交
register_parser.add_argument('password', type = str, required = True, help = '必须输入密码', location = ['form'])
register_parser.add_argument('B_UID', type = str, required = True, help = '必须输入BILIBILI平台UID', location = ['form'])
register_parser.add_argument('icon', type = FileStorage, location = ['files'])  # 添加图片


class RegisterApi(Resource):  # ----->类视图
    def post(self):
        args = register_parser.parse_args()  # --->获取数据
        username = args.get('username')
        password = args.get('password')
        B_UID = args.get('B_UID')
        icon = args.get('icon')
        name = User.query.filter(User.username == username).first()
        if name is not None:
            return {
                'status': 400,
                'message': 'This username has been registered,try again'
            }
        user = User()
        user.username = username
        user.password = password
        if icon:
            upload_path = os.path.join(Config.UPLOAD_ICON_DIR, icon.filename)
            icon.save(upload_path)
            user.icon = upload_path
        if B_UID:
            user.B_UID = B_UID
        db.session.add(user)
        db.session.commit()
        return {
            'status': 200,
            'message': 'Success to register'
        }


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
                'message': 'User no exist'
            }
        if check_name.password == password:
            return {
                'status': 200,
                'message': 'Success to login'
            }
        else:
            return {
                'status': 400,
                'message': 'Wrong password'
            }


api.add_resource(RegisterApi, '/register')
api.add_resource(LoginApi, '/login')
