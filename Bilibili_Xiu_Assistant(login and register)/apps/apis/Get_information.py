# encoding:utf-8
import os.path

from flask import Blueprint
from flask_restful import Resource, fields, reqparse, Api
from werkzeug.datastructures import FileStorage

from apps.models.user_model import User
from exits import db
from settings import Config