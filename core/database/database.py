from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.engine import Engine
from .base import Base
from .. import config

def create_database() -> Engine:
    """Создание движка базы данных и создание всех таблиц"""
    engine = create_engine(config.DATABASE_URL, echo=False, future=True)
    Base.metadata.create_all(engine)
    return(engine)


def create_session(engine: Engine) -> Session:
    """Создание сессии"""
    session = sessionmaker(engine, expire_on_commit=False)
    return(session)