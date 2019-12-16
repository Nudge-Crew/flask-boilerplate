from flask import Blueprint
from flask_restful import Api

from app.resources import user_resource

USER_BLUEPRINT = Blueprint("users", __name__)
api = Api(USER_BLUEPRINT)
api.add_resource(
    user_resource, "/users", "/users/<string:first_name>/<string:last_name>/<string:email>"
)