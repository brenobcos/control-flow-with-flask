from app.configs.database import db
from sqlalchemy import Column, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship
from dataclasses import dataclass


@dataclass
class Order(db.Model):
    order_id: int
    order_date: str

    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True)
    order_date = Column(DateTime, nullable=False)

    customer_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)

    curstomer = relationship("User", back_populates="orders")