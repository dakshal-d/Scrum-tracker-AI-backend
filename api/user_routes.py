import bcrypt
import jwt
from flask import Blueprint, jsonify, request

from api.auth import utc_now
from api.config import JWT_EXPIRES_IN, JWT_SECRET
from api.db import users_collection


user_blueprint = Blueprint("user", __name__, url_prefix="/user")


@user_blueprint.get("/")
def get_users():
    return "All the user"


@user_blueprint.post("/register")
def register():
    body = request.get_json(silent=True) or {}
    name = body.get("name")
    email = body.get("email")
    password = body.get("password")

    if users_collection.find_one({"email": email}):
        return jsonify(
            {"message": "An account with this email already exists", "status": 0}
        )

    try:
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt(5))
        users_collection.insert_one(
            {
                "name": name,
                "email": email,
                "password": hashed_password.decode("utf-8"),
                "date": utc_now(),
            }
        )
        return jsonify({"message": "User created", "status": 1})
    except Exception as error:
        return jsonify({"message": str(error), "status": 0})


@user_blueprint.post("/login")
def login():
    body = request.get_json(silent=True) or {}
    email = body.get("email")
    password = body.get("password")

    try:
        user = users_collection.find_one({"email": email})
        if not user:
            return jsonify({"message": "User does not exist", "status": 0})

        is_valid_password = bcrypt.checkpw(
            password.encode("utf-8"), user["password"].encode("utf-8")
        )
        if not is_valid_password:
            return jsonify({"message": "Incorrect password", "status": 0})

        expires_at = utc_now() + JWT_EXPIRES_IN
        token = jwt.encode({"userId": str(user["_id"]), "exp": expires_at}, JWT_SECRET)
        return jsonify(
            {
                "message": "User logged in successfully",
                "token": token,
                "status": 1,
            }
        )
    except Exception as error:
        return jsonify({"message": str(error), "status": 0})

