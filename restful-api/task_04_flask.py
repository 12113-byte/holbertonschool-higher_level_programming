#!/usr/bin/python3

from flask import Flask, jsonify, request

app = Flask(__name__)
users = {
    "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}
    }


@app.route("/")
def home():
    return "<p>Welcome to the Flask API!</p>"


@app.route("/data")
def data():
    return jsonify(list(users.keys()))


if __name__ == "__main__":
    app.run()


@app.route("/status")
def status():
    return "OK"


@app.route("/users/<username>")
def show_user_profile(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username") if data else None
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = data
    return jsonify({"message": "User added", "user": data})
