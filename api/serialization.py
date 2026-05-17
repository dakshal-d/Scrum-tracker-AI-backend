from bson import ObjectId


def serialize_document(document):
    serialized = {}
    for key, value in document.items():
        if isinstance(value, ObjectId):
            serialized["_id" if key == "_id" else key] = str(value)
        else:
            serialized[key] = value
    return serialized

