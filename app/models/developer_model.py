from app import db


class DeveloperModel(db.Model):
    __tablename__ = "developer"

    id = db.Table(db.BigInteger, primary_key=True)
    title = db.Table(db.String(30), nullable=False, unique=True)
    games = db.relationship("GameModel", lazy=True)

    def __init__(self, title):
        self.title = title

    def as_json(self):
        return {
            "id": self.id,
            "title": self.title
        }

    def __repr__(self):
        return f"<developer: {self.id}/{self.title}>"
