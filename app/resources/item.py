from sqlalchemy.sql.expression import func
from flask_restful import Resource, reqparse
from flask import jsonify
from flask_jwt_extended import jwt_required

from app.utils.check_privileges import privileged_user_required
from app.models.item import ItemModel
from app.utils.db import *
from app.utils.requests import *
from app import db


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("title", type=str, required=True)
    parser.add_argument("price", type=float, required=True)
    parser.add_argument("description", type=str, required=True)
    parser.add_argument("image", type=str)
    parser.add_argument("developer_id", type=int, required=True)

    def __get_all_items(self):
        items = ItemModel.query.order_by(func.random()).limit(10).all()
        items = [i.as_json() for i in items]

        return jsonify(items)

    def get(self, id=None):
        if not id:
            return self.__get_all_items()

        item = ItemModel.query.filter_by(id=id).first()

        if item:
            return jsonify(item.as_json())
        abort(404, message=f"Item with id {id} doesn't exists")

    @jwt_required()
    @privileged_user_required(role="admin")
    def post(self):
        data = get_data_and_abort_if_exists(Item.parser, ItemModel, "title")

        data["score"] = 0.0
        new_item = ItemModel(**data)
        try_to_add_and_commit(new_item)

        return {"message": "Added successfully"}, 201

    @jwt_required()
    @privileged_user_required(role="admin")
    def put(self, id):
        data = Item.parser.parse_args()

        entry = ItemModel.query.filter_by(id=id).first()
        if not entry:
            abort(404, message=f"Item doesn't exists")

        for key, value in data.items():
            if value is not None:
                setattr(entry, key, value)

        try_to_commit()

        return {"message": "Updated successfully"}, 200

    @jwt_required()
    @privileged_user_required(role="admin")
    def delete(self, id):
        item = ItemModel.query.filter_by(id=id).first()
        if not item:
            abort(404, message="Item doesn't exists")

        try:
            db.session.delete(item)
            db.session.commit()
        except Exception as exc:
            raise_server_error(exc)

        return {"message": "Item deleted successfully"}, 204
