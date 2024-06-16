from flask import request
from app.utils.db import is_entry_exists
from flask_smorest import abort


def get_data_from_request():
    match request.headers.get("Content-Type"):
        case "application/json":
            return request.json
        case "application/x-www-form-urlencoded":
            return request.form
        case _:
            return None


def get_data_and_abort_if_exists(parser, model, check_field):
    data = parser.parse_args()

    if is_entry_exists(model, title=data[check_field]):
        abort(400, message="Value already exists")

    return data
