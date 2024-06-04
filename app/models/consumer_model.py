from app import db


class ConsumerModel(db.Model):
    __tablename__ = "consumer"

    id = db.Table(db.BigInteger, primary_key=True)
    nickname = db.Table(db.String(20), unique=True, nullable=False)
    email = db.Table(db.String(30), nullable=False)
    password = db.Table(db.String(64), nullable=False)

    def __init__(self, nickname, email, password):
        self.nickname = nickname
        self.email = email
        self.password = password

    def as_json(self):
        return {
            "id": self.id,
            "nickname": self.nickname,
            "email": self.email,
            "password": self.password
        }

    def __repr__(self):
        return f"<consumer: {self.id}/{self.nickname}>"
