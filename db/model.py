from .engine import Base
from sqlalchemy.orm import Mapped, MappedColumn
import string


class User(Base):
    __tablenaem__ = "users"
    id_user: Mapped[int | None] = MappedColumn(
        unique=True, default=None, nullable=False)
    username: Mapped[str | None] = MappedColumn(
        unique=True, nullable=True, default=f"user_guest{string.digits}")
    password: Mapped[str] = MappedColumn(default=None)
