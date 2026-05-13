from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db

from app.crud.product import (
    get_products,
    create_product
)

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.get("/")
async def products(
    db: AsyncSession = Depends(get_db)
):
    return await get_products(db)


@router.post("/")
async def add_product(
    data: dict,
    db: AsyncSession = Depends(get_db)
):
    return await create_product(db, data)