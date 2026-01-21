from datetime import datetime

ALLOWED_STATUS = {"todo", "in_progress", "done"}
ALLOWED_PRIORITY = {"low", "medium", "high"}


def build_task(
    task_id: str,
    title: str,
    status: str,
    priority: str,
    user_id: str
) -> dict:
    if not task_id or not title or not user_id:
        raise ValueError("task_id, title, and user_id are required")

    if status not in ALLOWED_STATUS:
        raise ValueError(f"Invalid status: {status}")

    if priority not in ALLOWED_PRIORITY:
        raise ValueError(f"Invalid priority: {priority}")

    return {
        "task_id": task_id,
        "title": title,
        "status": status,
        "priority": priority,
        "user_id": user_id,  # referenced, not embedded
        "created_at": datetime.utcnow()
    }