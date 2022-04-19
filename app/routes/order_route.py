from flask import Blueprint
from app.controllers.order_controller import retrieve_by_id, order_products

bp = Blueprint("orders", __name__, url_prefix="/orders")

bp.get("/<int:order_id>")(retrieve_by_id)
bp.get("/<int:order_id>/products")(order_products)
