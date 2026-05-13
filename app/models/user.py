from sqlalchemy import String
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)

    username: Mapped[str] = mapped_column(
        String,
        unique=True
    )

    password: Mapped[str] = mapped_column(String)

    profile = relationship(
        "Profile",
        back_populates="user",
        uselist=False
    )

    orders = relationship(
        "Order",
        back_populates="user"
    )