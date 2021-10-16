import sqlalchemy
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy_utils import create_database, database_exists
from typing import Tuple


def init_database(uri: str) -> Tuple[Engine, Session]:
    engine = sqlalchemy.create_engine(uri)
    if not database_exists(uri):
        create_database(uri)

    Session = sessionmaker(bind=engine)
    session = Session()
    return (engine, session)
