import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB = os.getenv("MONGO_DB")

if not MONGO_URI or not MONGO_DB:
    raise RuntimeError("MongoDB environment variables not set")

client = MongoClient(MONGO_URI)
db = client[MONGO_DB]

def init_indexes():
    db.tasks.create_index([("user_id", 1)])
    db.tasks.create_index([("user_id", 1), ("created_at", -1)])