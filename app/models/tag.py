from app import db


class TagModel(db.Model):
    __tablename__ = "tag"

    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(25), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)

    items = db.relationship("ItemModel", secondary="item_tag_rel", back_populates="tags")

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def as_json(self):
        return {
            "id": self.id,
            "name": self.name
        }

    def __repr__(self):
        return f"<genre {self.id}/{self.name}>"
