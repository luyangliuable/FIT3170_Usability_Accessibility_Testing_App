from flask import Flask, jsonify, request
from app import db


class UserModel:

    def signUpUser(self):
        json_response = request.json
        new_user = {
            "name": json_response["name"],
            "email": json_response["email"],
            "password": json_response["password"]
        }

        # Checking is user with email already exists
        if db.users.find_one({"email": new_user["email"]}):
            return jsonify({
                "ERROR": "A user with this email already exists. "
            }), 400

        # If all the checks are passed , insert user into database
        db.users.insert_one(new_user)

    def loginUser(self):
        json_response = request.json

        user_db = db.users.find_one({"email": json_response["email"]})

        if user_db and user_db["password"] == json_response["password"]:
            return jsonify({"Success": "User successfully logged in"}), 200

        return jsonify({
            "ERROR": "Couldn't find user in database or inavlid login details"
        }), 400
