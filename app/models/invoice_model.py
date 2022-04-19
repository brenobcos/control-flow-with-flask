from dataclasses import dataclass
from datetime import datetime as dt

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship

from app.configs.database import db


@dataclass
class Invoice(db.Model):

    invoice_id: int
    invoice_number: str
    release_time: str

    __tablename__ = "invoices"

    invoice_id = Column(Integer, primary_key=True)
    invoice_number = Column(String(63), unique=True)
    release_time = Column(DateTime, default=dt.now())

    # O unique do order_id que define o relacionamento 1:1
    order_id = Column(Integer, ForeignKey("orders.order_id"), unique=True)

    order = relationship("Order", backref=backref("invoice", uselist=False))
