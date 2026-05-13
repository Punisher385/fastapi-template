from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from app.db.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)

    username: Mapped[str]

    profile = relationship(
        "Profile",
        back_populates="user",
        uselist=False
    )

    orders = relationship(
        "Order",
        back_populates="user"
    )