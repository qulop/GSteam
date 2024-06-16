from flask_restful import abort
from loguru import logger
from hashlib import sha256
from app import db


def raise_server_error(exc) -> any:
    db.session.rollback()

    msg = f"Server internal error: {exc}"
    logger.error(msg)
    return abort(500, message=msg)


def compare_passwords(hashed: str, raw_password: str) -> bool:
    return hashed == sha256(raw_password.encode("UTF-8")).hexdigest()
