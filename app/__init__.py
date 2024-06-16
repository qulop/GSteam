from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager


app = Flask(__name__,
    template_folder="../templates", 
    static_folder="../static")
app.config.from_object("config")
app.config['PROPAGATE_EXCEPTIONS'] = True

api = Api(app)
db = SQLAlchemy(app)
jwt = JWTManager(app)

migrate = Migrate(app, db, "db_repo")
migrate.init_app(app, db)


from app.error_handlers import *
from app.models import *
from app.resources import *

api.add_resource(User, "/users/<int:id>", "/users/")
api.add_resource(UserLogin, "/login/")
api.add_resource(UserRegistration, "/registration/")
api.add_resource(Item, "/store/items/<int:id>", "/store/items/")
api.add_resource(Developer, "/developers/<int:id>", "/developers/")
api.add_resource(Cart, "/cart/")

with app.app_context():
    db.create_all()

    from app.fill_database import fill_defaults
    fill_defaults("static/data/db_fill.json")
