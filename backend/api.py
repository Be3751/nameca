from flask import Blueprint, request, send_from_directory
from flask_restful import Api, Resource
from models import get_all, insert
from werkzeug.utils import secure_filename # ファイル名をチェックする関数
from tempfile import mkstemp
import os
from PIL import Image
from io import BytesIO
import base64
import glob

api_bp = Blueprint('api', __name__, url_prefix='/api')

class Spam(Resource):
    def get(self):
        return [{'id': x.id, 'imgname': x.imgname, 'name': x.name, 'furigana': x.furigana, 'birthday': x.birthday, 'favorite': x.favorite, 'skills': x.skills} for x in get_all()]

class Info(Resource):
    def get(self):
        return 'hello'

    def post(self):
        # 新規レコードの作成
        card_info = {
            'imgname': request.form.get('imgname'),
            'name': request.form.get('name'),
            'furigana': request.form.get('furigana'),
            'birthday': request.form.get('birthday'),
            'favorite': request.form.get('favorite'),
            'skills': request.form.get('skills')
        }
        insert(card_info)

api = Api(api_bp)
api.add_resource(Spam, '/')
api.add_resource(Info, '/info')