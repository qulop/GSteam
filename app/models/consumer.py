from app import db


class ConsumerModel(db.Model):
    __tablename_ = "consumer"

    id = db.Column(db.BigInteger, primary_key=True)
    profile_name = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(64), nullable=False)

    cart = db.relationship("CartModel", back_populates="consumer", uselist=False)

    def __init__(self, profile_name, email, password):
        self.profile_name = profile_name
        self.email = email
        self.password = password

    def as_json(self):
        return {
            "id": self.id,
            "profileName": self.profile_name,
        }

    def __repr__(self):
        return f"<consumer: {self.id}/{self.profile_name}>"
