from app import db


class PlatformModel(db.Model):
    __tablename__ = "platform"

    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    vendor = db.Column(db.String(20), nullable=False, unique=True)

    items = db.relationship("ItemModel", secondary="item_platform_rel", back_populates="platforms")

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
