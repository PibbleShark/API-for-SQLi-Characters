from flask import Blueprint

from flask_restful import Resource, Api, reqparse, marshal_with, fields

from char_list import char_list

result_field = {'result': fields.String}


def sanitize_check(payload):
    unsanitized = any(char in payload for char in char_list)
    if unsanitized:
        return 'unsanitized'
    else:
        return 'sanitized'


class SQLChars(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'payload',
            required=True,
            help='no payload provided',
            location=['json']
        )
        super().__init__()

    @marshal_with(result_field)
    def post(self):
        args = self.reqparse.parse_args()
        return {'result': sanitize_check(str(args['payload']))}


sql_chars_api = Blueprint('SQL_chars', __name__)
api = Api(sql_chars_api)
api.add_resource(
    SQLChars,
    '/v1/sanitized/input/',
    endpoint='sanitized'
)
