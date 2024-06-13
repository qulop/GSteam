from flask_restful import abort
from loguru import logger
from app import db


def raise_server_error(exc):
    db.session.rollback()

    msg = f"Failed to update user: {exc}"
    logger.error(msg)
    return abort(500, message=msg)