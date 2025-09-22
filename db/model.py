from sqlmodel import SQLModel, Field
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Users(SQLModel, table=True):
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4, primary_key=True)
    username: str = Field(index=True)
    password: str = Field(index=True)
