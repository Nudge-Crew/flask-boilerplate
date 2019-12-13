from flask import Blueprint
from flask_restful import Api

from app.resources import user_resource

USER_BLUEPRINT = Blueprint("users", __name__)
Api(USER_BLUEPRINT).add_resource(
    user_resource, "/users/<string:first_name>/<string:last_name>"
)