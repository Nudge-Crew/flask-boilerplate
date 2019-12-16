from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument

from app.repositories import user_repository
from app.utils import param_parser


class user_resource(Resource):
    method_decorators = {'get': [all]}

    @staticmethod
    def all():
        return "Hallo Wereld"

    @staticmethod
    def get(first_name, last_name, email):
        user = user_repository.get(first_name=first_name, last_name=last_name, email=email)

        return jsonify({
            "user": user.json
        })

    @staticmethod
    @param_parser(
        Argument("access_token", location="json", required=True, help="Your Canvas Access Token")
    )
    def post(first_name, last_name, email, access_token):
        user = user_repository.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            access_token=access_token
        )

        return jsonify({
            "user": user.json
        })

    @staticmethod
    @param_parser(
        Argument("access_token", location="json", required=True, help="Your Canvas Access Token")
    )
    def put(first_name, last_name, email, access_token):
        user = user_repository.update(
            first_name=first_name,
            last_name=last_name,
            email=email,
            access_token=access_token
        )

        return jsonify({
            "user": user.json
        })
