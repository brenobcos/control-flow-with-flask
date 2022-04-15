from flask import Blueprint
from app.controllers.user_controller import retrieve_by_id, retrieve_user_orders, retrieve_user_invoices

bp = Blueprint("users", __name__, url_prefix="/users")

bp.get("/<int:user_id>")(retrieve_by_id)
bp.get("/<int:user_id>/orders")(retrieve_user_orders)
bp.get("/<int:user_id>/invoices")(retrieve_user_invoices)