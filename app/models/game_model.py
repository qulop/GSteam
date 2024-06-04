from app import db
from sqlalchemy.schema import CheckConstraint


class GameModel(db.Model):
    __tablename__ = "game"

    id = db.Table(db.BigInteger, primary_key=True)
    title = db.Table(db.String(20), nullable=False)
    price = db.Table(db.Numeric(5, 2), nullable=False, default=0)
    score = db.Table(db.Numeric(2, 1), CheckConstraint("score >= 0 AND score <= 5"), nullable=False, default=0)
    developer_id = db.Table(db.BigInteger,
                            db.ForeignKey("developer.id", onupdate="CASCADE", ondelete="CASCADE"))
    genre_id = db.Table(db.BigInteger,
                        db.ForeignKey("genre.id", onupdate="CASCADE", ondelete="CASCADE"))
    platform_id=  db.Table(db.BigInteger,
                           db.ForeignKey("platform.id", onupdate="CASCADE", ondelete="CASCADE"))

    def __init__(self, title, price, score):
        self.title = title
        self.price = price
        self.score = score

    def as_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "price": self.price,
            "score": self.score,
            "developer_id": self.developer_id,
            "genre_id": self.genre_id,
            "platform_id": self.platform_id
        }

    def __repr__(self):
        return f"<game: {self.id}/{self.title}>"
