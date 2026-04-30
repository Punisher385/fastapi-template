from app.schemas.user import UserCreate, UserUpdate

users_db = {}
user_id_counter = 1


def get_all_users():
    return list(users_db.values())


def get_user(user_id: int):
    return users_db.get(user_id)


def create_user(user: UserCreate):
    global user_id_counter
    new_user = user.dict()
    new_user["id"] = user_id_counter

    users_db[user_id_counter] = new_user
    user_id_counter += 1

    return new_user


def update_user(user_id: int, user: UserUpdate):
    if user_id not in users_db:
        return None

    stored_user = users_db[user_id]

    update_data = user.dict(exclude_unset=True)

    stored_user.update(update_data)
    users_db[user_id] = stored_user

    return stored_user


def delete_user(user_id: int):
    return users_db.pop(user_id, None)