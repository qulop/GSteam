import types
from migrate.versioning import api
from config import SQLALCHEMY_MIGRATE_REPO
from config import SQLALCHEMY_DATABASE_URI
from app import db


version = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO) + 1
migration = f"{SQLALCHEMY_MIGRATE_REPO}/versions/{version}_migration.py"

tmp_module = types.ModuleType("old_model")
old_model = api.create_model(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)

exec(old_model, tmp_module.__dict__)
script = api.make_update_script_for_model(SQLALCHEMY_DATABASE_URI,
    SQLALCHEMY_MIGRATE_REPO, tmp_module.meta, db.metadata)

with open(migration, "wt") as f:
    f.write(script)

api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)

current_version = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
print(f"New migration saved as {migration}")
print(f"Current DB version: {str(current_version)}")