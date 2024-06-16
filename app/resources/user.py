from flask_restful import Resource, reqparse
from flask_smorest import abort
from flask import jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.utils.utils import raise_server_error, compare_passwords
from sqlalchemy.sql.expression import func
from hashlib import sha256

from app.models.user import UsersModel
from app.resources.cart import create_new_cart, delete_related_cart
from app.utils.db import *
from app import db


class Parser:
    parser = reqparse.RequestParser()
    parser.add_argument("name", type=str, required=True)
    parser.add_argument("email", type=str, required=True)
    parser.add_argument("password", type=str, required=True)
    parser.add_argument("role", type=str)


class User(Resource):
    parser = Parser.parser.copy()
    parser.replace_argument("name", type=str)
    parser.replace_argument("email", type=str)
    parser.replace_argument("password", type=str)

    def __get_all_users(self):
        users = UsersModel.query.order_by(func.random()).limit(10).all()
        users = [u.as_json() for u in users]

        return jsonify(users)

    def get(self, id=None):
        if not id:
            return self.__get_all_users()

        user = UsersModel.query.filter_by(id=id).first()

        if user:
            return jsonify(user.as_json())
        abort(404, message=f"User with id {id} doesn't exists")

    @jwt_required()
    def put(self, id):
        if get_jwt_identity() != id:
            abort(401, message="ID from JWT token doesn't match with ID from PUT-Request")

        data = User.parser.parse_args()

        user = UsersModel.query.filter_by(id=id).first()
        if not user:
            abort(404, message=f"User with id {id} doesn't exists")

        for key, value in data:
            if key == "password":
                value = sha256(value.encode("utf-8")).hexdigest()
            setattr(user, key, value)

        try_to_commit()

        return {"message": f"User with id {id} updated successfully"}, 200

    @jwt_required()
    def delete(self, id):
        if get_jwt_identity() != id:
            abort(401, message=f"ID from JWT token doesn't match with ID from DELETE-Request")

        user = UsersModel.query.filter_by(id=id).first()
        if not user:
            abort(400, message=f"User with id {id} doesn't exists")

        try:
            db.session.delete(user)
            delete_related_cart(user.id)
            db.session.commit()
        except Exception as exc:
            raise_server_error(exc)

        return {"message": f"User with id {id} deleted successfully"}, 204


class UserLogin(Resource):
    def post(self):
        data = User.parser.parse_args()

        user = UsersModel.query.filter_by(profile_name=data["name"]).one_or_none()
        if not user:
            abort(404, message=f"User {data['name']} not found")
        elif not compare_passwords(user.password, data["password"]):
            abort(401, message=f"Incorrect password")

        token = create_access_token(identity=user.id)
        return jsonify(access_token=token)


class UserRegistration(Resource):
    def post(self):
        data = Parser.parser.parse_args()

        exists = UsersModel.query.filter(UsersModel.profile_name == data["name"]).first()
        if exists:
            abort(400, message="User already exists")

        data["password"] = sha256(data["password"].encode("utf-8")).hexdigest()
        try:
            new_user = UsersModel(**data)

            db.session.add(new_user)
            create_new_cart(new_user)

            db.session.commit()

        except Exception as exc:
            raise_server_error(exc)

        return {"message": f"User({data['name']}) registration success"}, 201
