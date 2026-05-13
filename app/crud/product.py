from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.product import Product


async def get_products(db: AsyncSession):
    result = await db.execute(
        select(Product)
    )

    return result.scalars().all()


async def create_product(
    db: AsyncSession,
    data: dict
):
    product = Product(**data)

    db.add(product)

    await db.commit()

    await db.refresh(product)

    return product
