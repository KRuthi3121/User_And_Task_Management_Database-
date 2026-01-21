from datetime import datetime


def build_user(user_id: str, name: str, email: str) -> dict:
    if not user_id or not name or not email:
        raise ValueError("user_id, name, and email are required")

    return {
        "user_id": user_id,
        "name": name,
        "email": email,
        "created_at": datetime.utcnow()
    }