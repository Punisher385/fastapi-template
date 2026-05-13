from sqlalchemy import ForeignKey

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from app.db.base import Base


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str]

    price: Mapped[int]

    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id")
    )

    category = relationship(
        "Category",
        back_populates="products"
    )