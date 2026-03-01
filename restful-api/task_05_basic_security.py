#!/usr/bin/python3

from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config['JWT_SECRET_KEY'] = 'super-secret'
jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password", method="pbkdf2:sha256"),
        "role": "user"
        },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password", method="pbkdf2:sha256"),
        "role": "admin"
        }
}


@auth.verify_password
def verify_password(username, password):
    if username in users:
        stored_hash = users[username]["password"]
        if check_password_hash(stored_hash, password):
            return users[username]
    return None


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data["username"] if data else None
    password = data["password"] if data else None

    if username in users:
        stored_hash = users.get(username, {}).get("password")

        if check_password_hash(stored_hash, password):
            access_token = create_access_token(identity=username)
            return jsonify(access_token=access_token)

    return jsonify({"msg": "Bad username or password"}), 401


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    role = users[current_user]["role"]

    if role == "admin":
        return "Admin Access: Granted"
    else:
        return jsonify({"error": "Admin access required"}), 403


if __name__ == "__main__":
    app.run
