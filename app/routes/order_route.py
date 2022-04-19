from flask import Blueprint

from app.controllers.order_controller import order_products, retrieve_by_id

bp = Blueprint("orders", __name__, url_prefix="/orders")

bp.get("/<int:order_id>")(retrieve_by_id)
bp.get("/<int:order_id>/products")(order_products)
