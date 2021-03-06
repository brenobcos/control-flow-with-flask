from dataclasses import dataclass

from sqlalchemy import Column, ForeignKey, Integer, Numeric, String

from app.configs.database import db


@dataclass
class OrderProduct(db.Model):
    register_id: int
    sale_value: float

    __tablename__ = "orders_products"

    register_id = Column(Integer, primary_key=True)
    sale_value = Column(Numeric(asdecimal=False))

    order_id = Column(Integer, ForeignKey("orders.order_id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.product_id"), nullable=False)
