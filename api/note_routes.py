from bson import ObjectId
from flask import Blueprint, jsonify, request

from api.auth import require_auth
from api.db import notes_collection
from api.serialization import serialize_document


note_blueprint = Blueprint("note", __name__, url_prefix="/note")


@note_blueprint.before_request
@require_auth
def authenticate_note_routes():
    return None


@note_blueprint.get("")
def get_notes():
    try:
        notes = notes_collection.find({"user": request.user_id})
        return jsonify(
            {
                "data": [serialize_document(note) for note in notes],
                "message": "Success",
                "status": 1,
            }
        )
    except Exception as error:
        return jsonify({"message": str(error), "status": 0})


@note_blueprint.post("/create")
def create_note():
    body = request.get_json(silent=True) or {}
    body["user"] = request.user_id

    try:
        notes_collection.insert_one(body)
        return jsonify({"message": "Note created", "status": 1})
    except Exception as error:
        return jsonify({"message": str(error), "status": 0})


@note_blueprint.patch("")
def update_note():
    note_id = request.headers.get("id")
    body = request.get_json(silent=True) or {}
    body["user"] = request.user_id

    try:
        notes_collection.find_one_and_update({"_id": ObjectId(note_id)}, {"$set": body})
        return jsonify({"message": "Note updated", "status": 1})
    except Exception as error:
        return jsonify({"message": str(error), "status": 0})


@note_blueprint.delete("")
def delete_note():
    note_id = request.headers.get("id")

    try:
        notes_collection.find_one_and_delete({"_id": ObjectId(note_id)})
        return jsonify({"message": "Note deleted", "status": 1})
    except Exception as error:
        return jsonify({"message": str(error), "status": 0})
