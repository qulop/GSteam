from app.models.item import ItemModel
from app.models.consumer import ConsumerModel
from app.models.developer import DeveloperModel
from app.models.cart import CartModel

from app import db as _db


cart_item_rel = _db.Table("cart_item_rel",
    _db.Column("cart_id", _db.BigInteger,
               _db.ForeignKey("cart.id", onupdate="CASCADE", ondelete="CASCADE"), primary_key=True),
    _db.Column("item_id", _db.BigInteger,
               _db.ForeignKey("item.id", onupdate="CASCADE", ondelete="CASCADE"), primary_key=True)
)
