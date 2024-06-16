from app import db
from app.utils import raise_server_error


def try_to_add_and_commit(*args):
    try:
        for i in args:
            db.session.add(i)
        db.session.commit()
    except Exception as exc:
        raise_server_error(exc)


def try_to_commit():
    try:
        db.session.commit()
    except Exception as exc:
        raise_server_error(exc)


def is_entry_exists(model, **kwargs):
    entry = model.query.filter_by(**kwargs).first()

    return bool(entry)
