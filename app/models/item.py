from app import db
from sqlalchemy.schema import CheckConstraint


class ItemModel(db.Model):
    __tablename__ = "item"

    id = db.Column(db.BigInteger, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Numeric(5, 2), nullable=False, default=0)
    score = db.Column(db.Numeric(2, 1), CheckConstraint("score >= 0 AND score <= 5"), nullable=False, default=0)
    description = db.Column(db.Text, nullable=False)
    developer_id = db.Column(db.BigInteger,
        db.ForeignKey("developer.id", onupdate="CASCADE", ondelete="CASCADE"))

    carts = db.relationship("CartModel", secondary="cart_item_rel", back_populates="items")
    tags = db.relationship("TagModel", secondary="item_tag_rel", back_populates="items")
    platform = db.relationship("PlatformModel", secondary="item_platform_rel", back_populates="items")
    developer = db.relationship("DeveloperModel", back_populates="items")

    def __init__(self, title, price, score, developer_id):
        self.title = title
        self.price = price
        self.score = score
        self.developer_id = developer_id

    def as_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "price": self.price,
            "score": self.score,
            "description": self.description,
            "developerId": self.developer_id,
            "tags": [t.json() for t in self.tags.all()],
            "platforms": [p.json() for p in self.platform.all()]
        }

    def __repr__(self):
        return f"<game: {self.id}/{self.title}>"
