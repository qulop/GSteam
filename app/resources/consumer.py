from flask_restful import Resource, reqparse
from flask_smorest import abort
from flask import jsonify
from app.utils.utils import raise_server_error
import hashlib

from app.models.consumer import ConsumerModel
from app import db


class Parser:
    parser = reqparse.RequestParser()
    parser.add_argument("name", type=str, required=True)
    parser.add_argument("email", type=str, required=True)
    parser.add_argument("password", type=str, required=True)


class Consumer(Resource):
    parser = Parser.parser.copy()
    parser.replace_argument("name", type=str)
    parser.replace_argument("email", type=str)
    parser.replace_argument("password", type=str)


    def get(self, id):
        user = ConsumerModel.query.filter_by(id=id).first()

        if user:
            return jsonify(user.as_json())
        abort(404, message=f"User with id {id} doesn't exists")

    def put(self, id):
        data = Consumer.parser.parse_args()

        user = ConsumerModel.query.filter_by(id=id).first()
        if not user:
            abort(400, message=f"User with id {id} doesn't exists")

        user.profile_name = data.get("name") or user.profile_name
        user.email = data.get("email") or user.email
        if data.get("password"):
            user.password = hashlib.sha256(data["password"].encode("utf-8")).hexdigest()

        try:
            db.session.commit()
        except Exception as exc:
            raise_server_error(exc)

        return {"message": f"User with id {id} updated successfully"}

    def delete(self, id):
        user = ConsumerModel.query.filter_by(id=id).first()
        if not user:
            abort(400, message=f"User with id {id} doesn't exists")

        try:
            db.session.delete(user)
            db.session.commit()
        except Exception as exc:
            raise_server_error(exc)

        return {"message": f"User with id {id} deleted successfully"}


class ConsumerRegistration(Resource):
    def post(self):
        data = Parser.parser.parse_args()

        exists = ConsumerModel.query.filter(ConsumerModel.profile_name == data["name"]).first()
        if exists:
            abort(400, message="User already exists")

        data["password"] = hashlib.sha256(data["password"].encode("utf-8")).hexdigest()
        try:
            new_user = ConsumerModel(**data)

            db.session.add(new_user)
            db.session.commit()

        except Exception as exc:
            raise_server_error(exc)

        return {"message": f"User({data['name']}) registration success"}
