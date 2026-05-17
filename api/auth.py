from datetime import datetime, timezone
from functools import wraps

import jwt
from flask import jsonify, request

from api.config import JWT_SECRET


def get_token_payload(token):
    return jwt.decode(token, JWT_SECRET, algorithms=["HS256"])


def require_auth(handler):
    @wraps(handler)
    def wrapper(*args, **kwargs):
        if request.method == "OPTIONS":
            return handler(*args, **kwargs)

        token = request.headers.get("Authorization")
        if not token:
            return jsonify({"message": "Token is not valid please login", "status": 2})

        try:
            payload = get_token_payload(token)
        except jwt.PyJWTError:
            return jsonify({"message": "Token is not valid please login", "status": 2})

        request.user_id = payload.get("userId")
        request.token_payload = payload
        return handler(*args, **kwargs)

    return wrapper


def utc_now():
    return datetime.now(timezone.utc)

