import flask
import flask_restful as rest
import flask_sqlalchemy as sql
from flask_migrate import Migrate


app = flask.Flask(__name__, 
    template_folder="../templates", 
    static_folder="../static")
app.config.from_object("config")

api = rest.Api(app)
db = sql.SQLAlchemy(app)


migrate = Migrate(app, db, "db_repo")
migrate.init_app(app, db)

from app import views
from app.models import *

with app.app_context():
    db.create_all()

    from app.fill_database import fill_defaults
    fill_defaults("static/data/db_fill.json")
