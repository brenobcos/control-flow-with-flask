from dataclasses import dataclass

from sqlalchemy import Column, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.configs.database import db


@dataclass
class Order(db.Model):
    order_id: int
    order_date: str
    # products = list

    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True)
    order_date = Column(DateTime, nullable=False)

    customer_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)

    customer = relationship("User", back_populates="orders")

    products = relationship("Product", secondary="orders_products")