# import numpy as np
# import matplotlib
# import matplotlib.pyplot as plt
# import pandas as pd
# import pymongo
from collections import Counter
from flask import render_template, Blueprint, jsonify, request, Response, send_file, redirect, url_for
# from redis import Redis
import os
# from celery.result import AsyncResult

# matplotlib.use('Agg')

# main_blueprint = Blueprint("main", __name__) #, static_folder='static')
###############################################################################
#                      Possible modules that can be used                       #
###############################################################################
# import tempfile
# import random
# import struct
# import pickle
# import zlib

# celery.conf.result_backend = os.environ['REDIS_URL']


main_blueprint = Blueprint("main", __name__) #, static_folder='static')

###############################################################################
#                                    Redis                                    #
###############################################################################
# print("Redis url is", os.environ['REDIS_URL'])
# redis = Redis.from_url(os.environ['REDIS_URL'])


# ###############################################################################
# #                                   Mongodb                                   #
# ###############################################################################
# print("mongo url is", os.environ['MONGO_URL'])
# try:
#     mongo = pymongo.MongoClient(os.environ['MONGO_URL'])
#     db = mongo.flashcards
#     mongo.server_info() # Triger exception if connection fails to the database
# except Exception as ex:
#     print('failed to connect', ex)

@main_blueprint.route('/', methods=["GET", "POST"])
def display_flask_working_state():
    return "Flask back-end is online."
