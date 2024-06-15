from flask import request
from flask_smorest import abort
from functools import wraps
from flask_jwt_extended import decode_token

from app.models.user import UsersModel
from loguru import logger


def __check_privileges_level(token, required_role):
    role_factor = {
        "user": 0,
        "moderator": 50,
        "admin": 100
    }

    try:
        payload = decode_token(token)
    except Exception as exc:
        abort(400, message=f"{exc}")

    user_id = payload["sub"]

    user = UsersModel.query.filter_by(id=user_id).first()
    if not user or role_factor[user.role.value] < role_factor[required_role]:
        return False
    return True


def privileged_user_required(role="moderator"):
    def wrapper(fun):
        @wraps(fun)
        def decorator(*args, **kwargs):
            token = request.headers.get("Authorization")
            if not token or not __check_privileges_level(token.split()[1], role):
                abort(403, message="The user does not have sufficient privileges to perform this operation")
            fun(*args, **kwargs)

        return decorator

    return wrapper
