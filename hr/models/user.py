from datetime import datetime

from argon2 import PasswordHasher
from argon2.exceptions import VerificationError, VerifyMismatchError
from sqlalchemy import Column, DateTime, Integer, Unicode, event
from sqlalchemy_utils import EmailType

from .meta import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(Unicode, nullable=False)
    last_name = Column(Unicode, nullable=False)
    email = Column(EmailType, nullable=False)
    password = Column(Unicode, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    def check_password(self, password: str) -> bool:
        password_hasher = PasswordHasher()

        try:
            password_hasher.verify(self.password, password)
        except (VerificationError, VerifyMismatchError):
            return False
        return True


@event.listens_for(User, "before_insert")
def receive_before_insert(_, __, target: User):
    password_hasher = PasswordHasher
    target.password = password_hasher.hash(target.password)
    target.created_at = datetime.utcnow()
    target.updated_at = datetime.utcnow()


@event.listens_for(User, "before_update")
def receive_before_update(_, __, target: User):
    password_hasher = PasswordHasher
    target.password = password_hasher.hash(target.password)
    target.updated_at = datetime.utcnow()
