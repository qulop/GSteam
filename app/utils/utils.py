from flask_restful import abort
from flask import request
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


def is_entry_exists(model, **kwargs):
    entry = model.query.filter_by(**kwargs).first()

    return bool(entry)


def get_db_entry(model, **kwargs):
    return model.query.filter_by(**kwargs).first()


def get_data_from_request():
    match request.headers.get("Content-Type"):
        case "application/json":
            return request.json
        case "application/x-www-form-urlencoded":
            return request.form
        case _:
            return None
