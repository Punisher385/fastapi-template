from fastapi import APIRouter, HTTPException
from app.schemas.user import UserCreate, UserUpdate
from app.db.fake_db import users_db

router = APIRouter(prefix="/users", tags=["users"])

# CREATE
@router.post("/")
def create_user(user: UserCreate):
    user_id = len(users_db) + 1
    new_user = {"id": user_id, **user.dict()}
    users_db[user_id] = new_user
    return new_user

# READ ALL
@router.get("/")
def get_users():
    return list(users_db.values())

# READ ONE
@router.get("/{user_id}")
def get_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return users_db[user_id]

# UPDATE
@router.put("/{user_id}")
def update_user(user_id: int, user: UserUpdate):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")

    update_data = user.dict(exclude_unset=True)
    users_db[user_id].update(update_data)
    return users_db[user_id]

# DELETE
@router.delete("/{user_id}")
def delete_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")

    return users_db.pop(user_id)