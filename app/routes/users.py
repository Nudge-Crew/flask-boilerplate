from flask import Blueprint

from app.resources import user_resource

USER_PREFIX = "users"

USER_BLUEPRINT = Blueprint(USER_PREFIX, __name__)


@USER_BLUEPRINT.route('/', methods=['GET'])
def all():
    """
    Returning a list of users
    ---
    responses:
        200:
            description: A list of users
            schema:
                $ref: '#/models/User'
    """
    return user_resource.all()


