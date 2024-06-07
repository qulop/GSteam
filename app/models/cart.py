from app import db


class CartModel(db.Model):
    __tablename__ = "cart"

    id = db.Column(db.BigInteger, primary_key=True)
    consumer_id = db.Column(db.BigInteger, db.ForeignKey("consumer.id", onupdate="CASCADE", ondelete="CASCADE"))

    consumer = db.relationship("ConsumerModel", back_populates="cart")
    items = db.relationship("ItemModel", secondary="cart_item_rel", back_populates="carts")

    def __init__(self, added_time, item_id, consumer_id):
        self.added_time = added_time
        self.item_id = item_id
        self.consumer_id = consumer_id

    def as_json(self):
        return {
            "id": self.id,
            "addedTime": self.added_time,
            "itemId": self.item_id,
            "consumerId": self.consumer_id
        }

    def __repr__(self):
        return f"<cart: {self.id}/{self.consumer_id}"
