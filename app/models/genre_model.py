from app import db


class GenreModel(db.Model):
    __tablename__ = "genre"

    id = db.Table(db.BigInteger, primary_key=True)
    name = db.Table(db.String(25), unique=True, nullable=False)
    description = db.Table(db.Text, nullable=True)

    games = db.relationship("GameModel", lazy=True)

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def as_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }

    def __repr__(self):
        return f"<genre {self.id}/{self.name}>"
