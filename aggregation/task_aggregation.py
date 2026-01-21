from db.connection import db

def count_tasks_by_status(user_id: str):
    pipeline = [
        {"$match": {"user_id": user_id}},
        {"$group": {"_id": "$status", "count": {"$sum": 1}}}
    ]
    return list(db.tasks.aggregate(pipeline))

def fetch_recent_tasks(user_id: str, limit: int = 5):
    pipeline = [
        {"$match": {"user_id": user_id}},
        {"$sort": {"created_at": -1}},
        {"$limit": limit},
        {"$project": {"_id": 0}}
    ]
    return list(db.tasks.aggregate(pipeline))