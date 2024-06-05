from sqlalchemy import asc

from app import db
from app.models import ConsumerModel
from passlib.hash import pbkdf2_sha256
from flask_smorest import abort
from loguru import logger


def get_all_consumers():
    return ConsumerModel.query.order_by(asc(ConsumerModel.id)).all()


def get_consumer(consumer_id):
    return ConsumerModel.query.filter_by(id=consumer_id).first()


def register_consumer(data):
    nickname = data["nickname"]

    is_consumer_exists = ConsumerModel.query.filter(ConsumerModel.nickname == nickname).first()
    if is_consumer_exists:
        msg = "Consumer already exists!"
        logger.error(msg)
        abort(400, msg)

    email = data["email"]
    password = pbkdf2_sha256.hash(data["password"])

    try:
        new_consumer = ConsumerModel(nickname, email, password)

        db.session.add(new_consumer)
        db.session.commit()

    except Exception as ex:
        db.session.rollback()
        msg = "Failed to register consumer!"
        logger.error(msg)
        abort(400, msg)

    return {"message": "register consumer successful"}


def update_consumer(data, consumer_id):
    consumer = ConsumerModel.query.filter_by(id=consumer_id).first()
    if not consumer:
        msg = "Faled to update consumer: consumer doesn't exist!"
        logger.error(msg)
        abort(400, message=msg)

    nickname = data["nickname"]
    password = data["password"]
    email = data["email"]

    try:
        if nickname:
            consumer.nickname = nickname
        if password:
            consumer.password = pbkdf2_sha256.hash(password)
        if email:
            consumer.email = email

        db.session.commit()
    except Exception as ex:
        db.session.rollback()

        msg = f"Failed to update consumer: {ex}"
        logger.error(msg)
        abort(400, message=msg)

    return {"message": "Update consumer successfully"}
    

def delete_consumer(consumer_id):
    result = ConsumerModel.query.filter_by(id=consumer_id).delete()
    if not result:
        msg = "Failed to delete consumer: doesn't exists!"
        logger.error(msg)
        abort(400, message=msg)

    db.session.commit()

    return {"message": "Delete consumer successfully"}


    

