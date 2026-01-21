from db.connection import db, init_indexes
from crud.user_crud import create_user
from crud.task_crud import create_task


def seed():
    # Ensure indexes exist
    init_indexes()

    # Reset data to avoid duplicates
    db.users.delete_many({})
    db.tasks.delete_many({})

    # Users
    users = [
        ("u1", "Kruthi", "kruthi@test.com"),
        ("u2", "Alex", "alex@test.com"),
        ("u3", "Sam", "sam@test.com"),
        ("u4", "Nina", "nina@test.com"),
        ("u5", "Ravi", "ravi@test.com"),
        ("u6", "Emma", "emma@test.com"),
        ("u7", "Leo", "leo@test.com"),
    ]

    for user in users:
        create_user(*user)

    # Tasks
    tasks = [
        ("t1", "Setup MongoDB", "todo", "high", "u1"),
        ("t2", "Design schema", "in_progress", "medium", "u1"),
        ("t3", "Write aggregations", "done", "low", "u1"),

        ("t4", "Optimize indexes", "todo", "high", "u2"),
        ("t5", "Deploy service", "in_progress", "high", "u2"),
        ("t6", "Monitor logs", "done", "low", "u2"),

        ("t7", "Fix bugs", "todo", "high", "u3"),
        ("t8", "Write tests", "in_progress", "medium", "u3"),
        ("t9", "Refactor code", "done", "low", "u3"),

        ("t10", "Update docs", "todo", "medium", "u4"),
        ("t11", "Review PRs", "in_progress", "medium", "u4"),
        ("t12", "Release build", "done", "high", "u4"),

        ("t13", "Data cleanup", "todo", "low", "u5"),
        ("t14", "Improve queries", "in_progress", "high", "u5"),
        ("t15", "Performance test", "done", "medium", "u5"),

        ("t16", "Security audit", "todo", "high", "u6"),
        ("t17", "Patch dependencies", "in_progress", "medium", "u6"),
        ("t18", "Incident review", "done", "low", "u6"),

        ("t19", "Roadmap planning", "todo", "medium", "u7"),
        ("t20", "Sprint retro", "done", "low", "u7"),
    ]

    for task in tasks:
        create_task(*task)

    # Automatic verification
    user_count = db.users.count_documents({})
    task_count = db.tasks.count_documents({})

    print(f"{user_count} users and {task_count} tasks inserted")


if __name__ == "__main__":
    seed()