from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy.exc import NoResultFound
from flask_smorest import abort
from flask import jsonify

from app.models.cart import CartModel
from app.models.item import ItemModel
from app.utils.db import *


class Cart(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("item_id", type=int, required=True)

    def __get_cart_for_user(self, jwt_identity):
        cart = CartModel.query.get(jwt_identity)
        if not cart:
            abort(404, message=f"Cart doesn't exists")

        return cart

    @jwt_required()
    def get(self):
        cart = self.__get_cart_for_user(get_jwt_identity())

        items_in_cart = [i.as_json() for i in cart.items]
        return jsonify(items_in_cart)

    @jwt_required()
    def delete(self):
        cart = self.__get_cart_for_user(get_jwt_identity())

        cart.items.clear()
        try_to_commit()

        return {"message": "Cart clear success"}, 200

    @jwt_required()
    def put(self):
        data = Cart.parser.parse_args()
        cart = self.__get_cart_for_user(get_jwt_identity())

        item = ItemModel.query.get(data["item_id"])
        if not item:
            abort(404, message=f"Item from request doesn't exists")

        cart.items.append(item)
        try_to_commit()

        return {"message": "Updated successfully"}, 200


def delete_related_cart(user_id):
    related_cart = CartModel.query.filter_by(user_id=user_id)
    if not related_cart:
        raise NoResultFound(f"Cannot find related cart to user with ID {user_id}")

    db.session.delete(related_cart)


def create_new_cart(user):
    # There is no need for a try/except block,
    # since errors are caught in the ConsumerRegistration.post() method
    cart = CartModel(user)
    db.session.add(cart)
