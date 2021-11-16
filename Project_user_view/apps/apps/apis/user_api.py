# encoding:utf-8
import random
from linecache import cache

from flask import Blueprint, session
from flask_restful import Api, Resource, reqparse, inputs, fields, marshal

from apps.models.user_model import User
from exits import db

user_bp = Blueprint('user', __name__)
api = Api(user_bp)

sms_parser = reqparse.RequestParser()
sms_parser.add_argument('mobile', type = inputs.regex(r'1[356789]\d{9}$'), help = '手机号码格式错误', required = True
                        )


class SendMessageApi(Resource):
    def post(self):
        args = sms_parser.parse_args()
        mobile = args.get('mobile')
        return {'code': 200, 'msg': '验证码发送成功'}


# 订制输入
lr_parser = sms_parser.copy()
lr_parser.add_argument('code', type = str, help = '必须输入四位验证码', required = True, location = 'form')

# 订制输出
user_fields = {
    'id': fields.Integer,
    'username': fields.String
}


class LoginAndRegisterApi(Resource):
    def post(self):
        args = lr_parser.parse_args()
        mobile = args.get('mobile')
        code = args.get('code')
        if code == '1234':
            users = User.query.filter(User.phone == mobile).first()
            if not users:
                user = User()
                user.phone = mobile
                s = ''
                for i in range(13):
                    ran = random.randint(0, 9)
                    s += str(ran)
                user.username = '用户' + s
                db.session.add(user)
                db.session.commit()
                cache.get(mobile + "_", 1)
            return marshal(users, user_fields)  # 灵活，不用统一装饰器
        else:
            return {'errmsg': '验证码错误', 'status': 400}


# 忘记密码
class ForgetPassWordApi(Resource):
    def get(self):
        s = 'QWERTYUIOPASDFGHJKLZXCVBNMmnbvcxzlkjhgfdsapoiuytrewq1234567890'
        code = ''
        for i in range(4):
            ran = random.choice(s)
            code += ran
        # 保存code
        # cache.set('',code)
        session['code'] = code
        return {'code': code}


# 重置密码输入
reset_parser = sms_parser.copy()
reset_parser.add_argument('image_code', type =str, help = '请输入正确格式的验证码', required = True)


class ResetPasswordApi(Resource):
    def get(self):
        args = reset_parser.parse_args()
        mobile = args.get('mobile')
        imagecode = args.get('image_code')
        code = session.get('code')
        print(imagecode)
        print(code)
        if code and imagecode.lower() == code.lower():
            user = User.query.filter(User.phone == mobile).first()
            # 发送手机验证码
            return {'code': 200, 'msg': '发送短信成功'}
        else:
            return {'status': 400, 'msg': '验证码输入错误'}


update_parser = reqparse.RequestParser()
update_parser.add_argument('code', type = inputs.regex(r'^\d{4}$'), help = '输入手机验证码', location = 'form')

api.add_resource(SendMessageApi, '/sms')
api.add_resource(LoginAndRegisterApi, '/code_login')
api.add_resource(ForgetPassWordApi, '/forget')
api.add_resource(ResetPasswordApi, '/reset')
