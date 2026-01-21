from db.connection import db
from models.user import build_user


def create_user(user_id: str, name: str, email: str) -> dict:
    user = build_user(user_id, name, email)
    db.users.insert_one(user)
    return user


def get_user(user_id: str) -> dict | None:
    return db.users.find_one(
        {"user_id": user_id},
        {"_id": 0}
    )