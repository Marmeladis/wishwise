from datetime import datetime, timezone
from typing import Optional
from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: int = Field(primary_key=True)
    email: Optional[str] = Field(
        max_length=255, unique=True, description="Email для авторизации"
    )
    password_hash: Optional[str] = Field(max_length=255)
    username: Optional[str] = Field(max_length=100)
    created_at: datetime = Field(default_factory=lambda: datetime.utcnow())
