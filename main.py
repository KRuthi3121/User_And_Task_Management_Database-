from db.connection import db
from crud.task_crud import (
    get_tasks_for_user,
    update_task_status_and_priority,
)
from aggregation.task_aggregation import (
    count_tasks_by_status,
    fetch_recent_tasks,
)

def run():
    users = db.users.find({}, {"_id": 0, "user_id": 1, "name": 1})

    for user in users:
        user_id = user["user_id"]
        name = user["name"]

        print(f"\nUser: {name} ({user_id})")
        print("Tasks:")
        tasks = get_tasks_for_user(user_id)
        print(tasks)

        print("Task count by status:")
        print(count_tasks_by_status(user_id))

        print("Most recent tasks:")
        print(fetch_recent_tasks(user_id))

    # Demonstrate atomic update explicitly
    print("\nAtomic update demo (t1 → done, high)")
    update_task_status_and_priority("t1", "done", "high")
    print(get_tasks_for_user("u1"))


if __name__ == "__main__":
    run()