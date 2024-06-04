import os

file_basedir = os.path.abspath(os.path.dirname(__file__))

host = "localhost"
port = 5432
db_name = "gsteam"

# SQLAlchemy config
SQLALCHEMY_DATABASE_URI = f"postgresql://{host}:{port}/{db_name}"
SQLALCHEMY_MIGRATE_REPO = 0

# App config
DEBUG = True
CSRF_ENABLED = True
SECRET_KEY = "2e083f994e609ed7527b112c5c9fc74e55359caae67bfdbc9d63c262b4f51e4d"
