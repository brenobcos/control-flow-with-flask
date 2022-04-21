from dataclasses import asdict
from http import HTTPStatus

from flask import jsonify, request, url_for

from app.exc import (
    IdNotFoundError,
    InvalidEmailError,
    InvalidDateFormatError,
    UnderageUserError,
)
from app.models.user_model import User
from app.services.query_service import get_by_id
from app.configs.database import db
from sqlalchemy.exc import IntegrityError
from psycopg2.errors import UniqueViolation


def create_user():
    data = request.get_json()

    try:
        user = User(**data)
    except InvalidEmailError:
        return {"error": "email must contain `churros`"}, HTTPStatus.BAD_REQUEST
    except InvalidDateFormatError:
        return {"error": "date format must be `YYYY/MM/DD`"}, HTTPStatus.BAD_REQUEST
    except UnderageUserError:
        return {"error": "user must be over 18 years old"}, HTTPStatus.BAD_REQUEST

    try:
        db.session.add(user)
        db.session.commit()
    except IntegrityError as e:
        if type(e.orig) == UniqueViolation:
            return {"error": "this email already exists"}, HTTPStatus.CONFLICT

    return jsonify(user), HTTPStatus.CREATED


def retrieve_by_id(user_id: int):
    try:
        user = get_by_id(User, user_id)
    except IdNotFoundError:
        return {"error": "id not found"}, HTTPStatus.NOT_FOUND

    serialized_user = {"orders": url_for(".retrieve_user_orders", user_id=user_id)}

    serialized_user.update(asdict(user))

    return jsonify(serialized_user), HTTPStatus.OK


def retrieve_user_orders(user_id: int):
    user = User.query.get(user_id)

    if not user:
        return {"error": "user id not found"}, HTTPStatus.NOT_FOUND

    return jsonify(user.orders), HTTPStatus.OK


def retrieve_user_invoices(user_id: int):
    user = User.query.get(user_id)

    if not user:
        return {"error": "user id not found"}, HTTPStatus.NOT_FOUND

    invoices_order = [order.invoice for order in user.orders]

    return jsonify(invoices_order), HTTPStatus.OK
