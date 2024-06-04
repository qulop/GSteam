import flask
import flask_restful as rest
import flask_sqlalchemy as sql

app = flask.Flask(__name__)
app.config.from_object("config")

api = rest.Api(app)
db = sql.SQLAlchemy(app)


from app import views
