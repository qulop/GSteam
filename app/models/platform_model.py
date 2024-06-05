from app import db


class PlatformModel(db.Model):
    __tablename__ = "platform"

    id = db.Table(db.BigInteger, primary_key=True)
    name = db.Table(db.String(20), nullable=False, unique=True)
    vendor = db.Table(db.String(20), nullable=False, unique=True)

    games = db.relationship("GameModel", lazy=True)

    def __init__(self, name, vendor):
        self.name = name
        self.vendor = vendor

    def as_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "vendor": self.vendor
        }

    def __repr__(self):
        return f"<platform: {self.id}/{self.name}>"
