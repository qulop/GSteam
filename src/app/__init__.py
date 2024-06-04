import flask
import flask_restful as rest

app = flask.Flask(__name__)
api = rest.Api(app)


from app import views
