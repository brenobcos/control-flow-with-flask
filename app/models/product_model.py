from app.configs.database import db
from sqlalchemy import Column, Integer, Numeric, String
from dataclasses import dataclass


@dataclass
class Product(db.Model):
    product_id: int
    name: str
    price: float

    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True)
    name = Column(String(50))
    price = Column(Numeric)
