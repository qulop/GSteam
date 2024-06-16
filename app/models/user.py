import enum
from app import db


class UserRole(enum.Enum):
    user = "user"
    moderator = "moderator"
    admin = "admin"


class UsersModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.BigInteger, primary_key=True)
    profile_name = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(64), nullable=False)
    role = db.Column(db.Enum(UserRole), nullable=False, default=UserRole.user)

    cart = db.relationship("CartModel", back_populates="user", uselist=False)

    def __init__(self, name, email, password, role=None):
        self.profile_name = name
        self.email = email
        self.password = password
        self.role = role

    def as_json(self):
        return {
            "id": self.id,
            "profileName": self.profile_name,
            "role": self.role.value
        }

    def __repr__(self):
        return f"<user: {self.id}/{self.profile_name}>"
