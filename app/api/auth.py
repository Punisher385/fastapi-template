from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Response

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db

from app.models.user import User

from app.schemas.auth import (
    RegisterSchema,
    LoginSchema
)

from app.auth.utils import (
    hash_password,
    verify_password,
    create_access_token
)

from app.auth.dependencies import get_current_user


router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post("/register")
async def register(
    data: RegisterSchema,
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(User).where(
            User.username == data.username
        )
    )

    existing_user = result.scalar()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="User already exists"
        )

    user = User(
        username=data.username,
        password=hash_password(data.password)
    )

    db.add(user)

    await db.commit()

    return {
        "message": "User created"
    }


@router.post("/login")
async def login(
    data: LoginSchema,
    response: Response,
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(User).where(
            User.username == data.username
        )
    )

    user = result.scalar()

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    if not verify_password(
        data.password,
        user.password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_access_token({
        "user_id": user.id
    })

    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True
    )

    return {
        "message": "Logged in"
    }


@router.get("/me")
async def me(
    current_user=Depends(get_current_user)
):

    return {
        "id": current_user.id,
        "username": current_user.username
    }


@router.get("/orders")
async def my_orders(
    current_user=Depends(get_current_user)
):

    return {
        "message": f"Orders of {current_user.username}"
    }