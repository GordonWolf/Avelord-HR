from sqlalchemy import Column, ForeignKey, Integer

from .meta import Base
from .user import User


class UserCode(Base):
    __tablename__ = "user_code"

    user = Column(
        Integer,
        ForeignKey(User.id),
        primary_key=True,
        nullable=False,
    )
    last_code = Column(Integer, nullable=False)
    current_code = Column(Integer, nullable=False)
