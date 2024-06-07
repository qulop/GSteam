from app import db


class DeveloperModel(db.Model):
    __tablename__ = "developer"

    id = db.Column(db.BigInteger, primary_key=True)
    title = db.Column(db.String(30), nullable=False, unique=True)

    items = db.relationship("ItemModel", back_populates="developer")

    def __init__(self, title):
        self.title = title

    def as_json(self):
        return {
            "id": self.id,
            "title": self.title
        }

    def __repr__(self):
        return f"<developer: {self.id}/{self.title}>"
