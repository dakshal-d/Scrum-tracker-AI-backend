from pymongo import MongoClient

from api.config import MONGO_CONNECTION_URL, MONGO_DB_NAME


if not MONGO_CONNECTION_URL:
    raise RuntimeError("MONGO_CONNECTION_URL is required")

client = MongoClient(MONGO_CONNECTION_URL, serverSelectionTimeoutMS=5000)
database = client.get_database(MONGO_DB_NAME)

users_collection = database["users"]
notes_collection = database["notes"]


def verify_connection():
    client.admin.command("ping")
