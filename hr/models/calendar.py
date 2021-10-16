import enum

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    SmallInteger,
    event,
)

from .meta import Base
from .user import User


class Check(enum.Enum):
    check_in = 0
    check_out = 1


class Calendar(Base):
    __tablename__ = "calendar"

    user = Column(
        Integer,
        ForeignKey(User.id),
        primary_key=True,
        nullable=False,
    )
    datetime = Column(DateTime, nullable=False)
    month = Column(SmallInteger, nullable=False)
    year = Column(SmallInteger, nullable=False)
    check = Column(Check, nullable=False)
    is_self_check = Column(Boolean, nullable=False)


@event.listens_for(User, "before_insert")
def receive_before_insert(_, __, target: Calendar):
    target.year = target.datetime.year
    target.month = target.datetime.month
