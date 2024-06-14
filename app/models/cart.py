from app import db
from app.models.user import UsersModel


class CartModel(db.Model):
    __tablename__ = "cart"

    id = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(db.BigInteger, db.ForeignKey("users.id", onupdate="CASCADE", ondelete="CASCADE"))

    user = db.relationship("UsersModel", back_populates="cart")
    items = db.relationship("ItemModel", secondary="cart_item_rel", back_populates="carts")

    def __init__(self, user):
        self.user = user

    def as_json(self):
        return {
            "id": self.id,
            "addedTime": self.added_time,
            "itemId": self.item_id,
            "userId": self.user_id
        }

    def __repr__(self):
        return f"<cart: {self.id}/{self.user_id}"
