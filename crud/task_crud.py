from db.connection import db
from models.task import build_task


def create_task(
    task_id: str,
    title: str,
    status: str,
    priority: str,
    user_id: str
) -> dict:
    task = build_task(task_id, title, status, priority, user_id)
    db.tasks.insert_one(task)
    return task


def get_tasks_for_user(user_id: str) -> list:
    return list(
        db.tasks.find(
            {"user_id": user_id},
            {"_id": 0}
        )
    )


def update_task_status_and_priority(
    task_id: str,
    status: str,
    priority: str
) -> bool:
    result = db.tasks.update_one(
        {"task_id": task_id},
        {"$set": {"status": status, "priority": priority}}
    )
    return result.modified_count == 1


def delete_task(task_id: str) -> bool:
    result = db.tasks.delete_one({"task_id": task_id})
    return result.deleted_count == 1