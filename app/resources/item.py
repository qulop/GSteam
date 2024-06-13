from flask_restful import Resource
from flask_smorest import abort
from flask import jsonify

from app.models.item import ItemModel


class ItemResource(Resource):
    def get(self, id):
        item = ItemModel.query.filter_by(id=id).first()

        if item:
            return jsonify(item.as_json())
        abort(404, message=f"Item with id {id} doesn't exists")
