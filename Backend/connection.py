import os
from pymongo import MongoClient

MONGO_URI = os.environ.get("MONGO_URI", "mongodb://localhost:27017/")
MONGO_DB = os.environ.get("MONGO_DB", "mydatabase")

client = MongoClient(MONGO_URI)
db = client[MONGO_DB]
users_collection = db["users"]