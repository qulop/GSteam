import sqlalchemy.exc

from app import db
import app.models
import json
import os


def fill_defaults(path: str) -> None:
    path = os.path.abspath(path)

    with open(path, "r") as f:
        json_file = json.load(f)

    for table_name, data in json_file.items():
        if table_name != "item":
            continue

        model_name = f"{table_name.capitalize()}Model"
        model_class_ref = getattr(app.models, model_name)

        for item in data:
            db_entry = model_class_ref(**item)
            db.session.add(db_entry)

            try:
                db.session.commit()
            except (sqlalchemy.exc.PendingRollbackError, sqlalchemy.exc.IntegrityError):
                print(f'Entry already exists in table "{table_name}" -- skip commit')
            except sqlalchemy.exc.DataError as err:
                print(f"SQLAlchemy DataError: {err}")
