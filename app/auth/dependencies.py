from jose import jwt, JWTError

from fastapi import Cookie, HTTPException

from sqlalchemy import select

from app.auth.utils import SECRET_KEY, ALGORITHM
from app.db.session import AsyncSessionLocal
from app.models.user import User


async def get_current_user(
    access_token: str = Cookie(default=None)
):

    if not access_token:
        raise HTTPException(
            status_code=401,
            detail="Not authenticated"
        )

    try:

        payload = jwt.decode(
            access_token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        user_id = payload.get("user_id")

    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    async with AsyncSessionLocal() as session:

        result = await session.execute(
            select(User).where(User.id == user_id)
        )

        user = result.scalar()

        if not user:
            raise HTTPException(
                status_code=401,
                detail="User not found"
            )

        return user