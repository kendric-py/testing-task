from ast import In
from enum import unique
from sqlalchemy import (
    Column, String, BigInteger, Integer, DateTime,
    Boolean, Float, Text, ForeignKey, Date
)
from .base import Base


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    price_usd = Column(Integer)
    delivery_time = Column(Date)
    price_rub = Column(Integer)