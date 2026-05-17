from flask import Flask, jsonify
from flask_cors import CORS

from api.config import PORT
from api.db import verify_connection
from api.note_routes import note_blueprint
from api.user_routes import user_blueprint


def create_app():
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    CORS(app)

    app.register_blueprint(user_blueprint)
    app.register_blueprint(note_blueprint)

    @app.get("/")
    def home():
        return jsonify({"message": "api is working now"})
    
    @app.get("/health")
    def health():
        return jsonify({"message": "health check is good"})

    @app.errorhandler(404)
    def not_found(_error):
        return "404 page not found"

    return app


app = create_app()


if __name__ == "__main__":
    try:
        verify_connection()
        print("database is connected")
    except Exception as error:
        print(error)

    print("Server is running on port number", PORT)
    app.run(host="0.0.0.0", port=PORT)
