import os
from datetime import timedelta

from dotenv import load_dotenv


load_dotenv()

MONGO_CONNECTION_URL = os.getenv("MONGO_CONNECTION_URL", "").strip()
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "test")
JWT_SECRET = os.getenv("JWT_SECRET", "dakshal")
JWT_EXPIRES_IN = timedelta(minutes=3)
PORT = int(os.getenv("PORT", "4000"))
