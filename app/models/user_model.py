from dataclasses import dataclass

from sqlalchemy import BigInteger, Boolean, Column, Date, Integer, Numeric, String
from sqlalchemy.orm import relationship, validates

from app.configs.database import db
from app.exc import InvalidEmailError, InvalidDateFormatError, UnderageUserError
from datetime import datetime as dt


@dataclass
class User(db.Model):
    user_id: int
    email: str
    birthdate: str
    children: int
    married: bool
    account_balance: float
    # orders: list

    __tablename__ = "users"

    user_id = Column(BigInteger, primary_key=True)
    email = Column(String(64), unique=True, nullable=False)
    birthdate = Column(Date, nullable=False)
    children = Column(Integer, default=0)
    married = Column(Boolean, default=False)
    account_balance = Column(Numeric(asdecimal=False))

    orders = relationship("Order", back_populates="customer", uselist=True)

    @validates("email")
    def validate_email(self, key, email_to_be_tested):
        if "churros" not in email_to_be_tested:
            raise InvalidEmailError
        return email_to_be_tested

    @validates("birthdate")
    def validate_birthdate(self, key, birthdate_to_be_tested):
        today = dt.now()
        try:
            b_date = dt.strptime(birthdate_to_be_tested, "%Y/%m/%d")
            year_diff = today.year - b_date.year
            month_day_diff = int((today.month, today.day) < (b_date.month, b_date.day))
            if (year_diff - month_day_diff) < 18:
                raise UnderageUserError


        except ValueError:
            raise InvalidDateFormatError
        return birthdate_to_be_tested
