# encoding:utf-8
from flask import Blueprint
from flask_restful import Api, Resource, reqparse, inputs

user_bp = Blueprint('user', __name__)
api = Api(user_bp)

# # # sms_parser = reqparse.RequestParser()
# # # sms_parser.add_argument('mobile', types = inputs.regex(r'1[356789]\d{9}$'), help = '手机号码格式错误', required = True,
# #                         )
#
#
# class SendMessageApi(Resource):
#     def post(self):
#         args = sms_parser.parse_args()
#         mobile = args.get('mobile')
