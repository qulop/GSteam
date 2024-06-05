import os

root_dir = os.path.abspath(os.path.dirname(__file__))

# SQLAlchemy config
SQLALCHEMY_DATABASE_URI = os.getenv("DB_URL")
SQLALCHEMY_MIGRATE_REPO = os.path.join(root_dir, "db_repo")

# App config
DEBUG = True
CSRF_ENABLED = True
SECRET_KEY = os.getenv("APP_SECRET_KEY")
