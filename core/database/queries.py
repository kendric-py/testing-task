from ast import Delete
from operator import or_
from sqlalchemy import select, delete, or_
from sqlalchemy.orm import Session
from .models import Order
from datetime import datetime


def merge_order(session: Session, id: int, price_usd: int, delivery_time: str, price_rub: int) -> Order:
    order = Order(
        id=id, price_usd=price_usd, delivery_time=delivery_time, price_rub=price_rub
    )
    session.merge(order)
    session.commit()
    return(order)


def get_order(session: Session, order_number: int) -> Order | None:
    query = select(Order).where(Order.order_number == order_number)
    response = session.execute(query)
    return(response.scalars().first())


def delete_not_sheet_orders(session: Session, sheet_orders: list[int]) -> list[Order]:
    query = delete(Order).where(Order.id.not_in(sheet_orders))
    session.execute(query)
    return(session.commit())
