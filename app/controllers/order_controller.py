from dataclasses import asdict
from http import HTTPStatus

from flask import jsonify, url_for
from ipdb import set_trace
from sqlalchemy.orm import Query, Session

from app.configs.database import db
from app.exc import IdNotFoundError
from app.models.order_model import Order
from app.models.order_product_model import OrderProduct
from app.models.product_model import Product
from app.services.query_service import get_by_id


def retrieve_by_id(order_id: int):
    try:
        order = get_by_id(Order, order_id)
    except IdNotFoundError:
        return {"error": "id not found"}, HTTPStatus.NOT_FOUND

    serialized_order = {"products": url_for(".order_products", order_id=order_id)}


    serialized_order.update(asdict(order))

    # set_trace()

    return jsonify(serialized_order), HTTPStatus.OK


def order_products(order_id: int):
    """
    SELECT
        p.product_id, p."name",
        op.sale_value
    FROM orders o
    JOIN orders_products op
        ON o.order_id = op.order_id
    JOIN products p
        ON p.product_id = op.product_id
    WHERE o.order_id = 2;
    """

    session: Session = db.session

    query: Query = (
        session.query(Product.product_id, Product.name, OrderProduct.sale_value)
        .select_from(Order)
        .join(OrderProduct)
        .join(Product)
        .filter(Order.order_id == order_id)
        .all()
    )

    print(f"{query=}")

    prodcuts = [product._asdict() for product in query]

    return jsonify(prodcuts), HTTPStatus.OK
