from flask import Flask
from flask import render_template, Blueprint, jsonify, request, Response, send_file, redirect, url_for
import os
import pymongo

from server.models.User import *

login_blueprint = Blueprint('login', __name__)

try:
    mongo = pymongo.MongoClient("mongodb://localhost:27017/")
    db = mongo.users_db
    mongo.server_info()  # Triger exception if connection fails to the database
except Exception as ex:
    print('failed to connect', ex)


@login_blueprint.route('/')
def home():
    return 'Flask with docker!'


@login_blueprint.route('/signUp', methods=['POST'])
def signUpUser():
    return UserModel().signUpUser()


@login_blueprint.route('/login', methods=['POST'])
def loginUser():
    return UserModel().loginUser()


if __name__ == "__main__":
    pass
    # login_blueprint.run(host="0.0.0.0", port=5002, debug=True)
