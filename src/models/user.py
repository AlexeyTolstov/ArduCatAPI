from db.base import Base
from typing import Annotated
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String


intpk = Annotated[int, mapped_column(primary_key=True)]


class UsersORM(Base):
    __tablename__ = "users"

    id: Mapped[intpk]
    login: Mapped[str] = mapped_column(String(256))
    password: Mapped[str] = mapped_column(String(256))

    first_name: Mapped[str] = mapped_column(String(256))
    last_name: Mapped[str] = mapped_column(String(256))
    email: Mapped[str] = mapped_column(String(256))