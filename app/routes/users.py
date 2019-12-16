from flask import Blueprint

from app.resources import user_resource

USER_PREFIX = "users"

USER_BLUEPRINT = Blueprint(USER_PREFIX, __name__)


@USER_BLUEPRINT.route('/', methods=['GET'])
def all():
    return user_resource.all()


