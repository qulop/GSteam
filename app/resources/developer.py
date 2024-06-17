from sqlalchemy.sql.expression import func
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from flask_smorest import abort
from flask import jsonify

from app.models.developer import DeveloperModel
from app.utils.check_privileges import privileged_user_required
from app.utils.db import *
from app.utils.requests import get_data_and_abort_if_exists


class Developer(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("title", type=str, required=True)

    def __get_all_developers(self):
        developers = DeveloperModel.query.order_by(func.random()).limit(10).all()
        developers = [d.as_json() for d in developers]

        return jsonify(developers)

    def get(self, id=None):
        if not id:
            return self.__get_all_developers()

        developer = DeveloperModel.query.filter_by(id=id).first()

        if developer:
            return jsonify(developer.as_json())
        abort(404, message=f"Developer with id {id} doesn't exists")

    @jwt_required()
    @privileged_user_required(role="admin")
    def post(self):
        data = get_data_and_abort_if_exists(Developer.parser, DeveloperModel, "title")

        new_dev = DeveloperModel(**data)
        try_to_add_and_commit(new_dev)

        return {"message": "Added successfully"}, 201

    @jwt_required()
    @privileged_user_required(role="admin")
    def put(self, id):
        data = Developer.parser.parse_args()

        entry = DeveloperModel.query.filter_by(id=id).first()
        if not entry:
            abort(404, message=f"Developer doesn't exists")

        for key, value in data.items():
            if value is not None:
                setattr(entry, key, value)

        try:
            db.session.commit()
        except Exception as exc:
            raise_server_error(exc)

        return {"message": "Updated successfully"}, 200

    @jwt_required()
    @privileged_user_required(role="admin")
    def delete(self, id):
        entry = DeveloperModel.query.filter_by(id=id).first()
        if not entry:
            abort(404, message="Developer doesn't exists")

        try:
            db.session.delete(entry)
            db.session.commit()
        except Exception as exc:
            raise_server_error(exc)

        return {"message": "Developer deleted successfully"}, 204
