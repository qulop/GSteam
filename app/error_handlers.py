from app import jwt
from flask import jsonify


@jwt.expired_token_loader
def token_expired(h, p):
    return jsonify(message="JWT token expired"), 401


@jwt.unauthorized_loader
def unauthorized(err):
    return jsonify(message="No JWT token provided"), 401