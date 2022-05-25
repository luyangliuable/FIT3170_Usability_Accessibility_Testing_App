from flask import Blueprint, request
from redis import Redis, StrictRedis
from fastapi import FastAPI
import pymongo
import warnings
import zlib
import uuid
import pickle
import io
import os
from PIL import Image
import shutil
import json

###############################################################################
#                          Docker dependent variables                         #
###############################################################################
host_for_docker = "0.0.0.0"
name = "scan_app"
signal_start_api_url = "send_uid"_

###############################################################################
#                           Create flask blueprint                           #
###############################################################################

scan_app_blueprint = Blueprint("scan_app", __name__)

###############################################################################
#                            Create websocket app                            #
###############################################################################

app = FastAPI()

###############################################################################
#                                Start mongodb                                #
###############################################################################

try:
    mongo = pymongo.MongoClient(
        host='localhost',
        port=27017,
    )

    mongo.server_info() # Triger exception if connection fails to the database
except Exception as ex:
    print('failed to connect', ex)

###############################################################################
#             Strict Redis forces redise to decode byte to string             #
###############################################################################
r = StrictRedis('localhost', 6379, decode_responses=True)

def unique_id_generator():
    res = "apk_file_" + str( uuid.uuid4() )
    return res


@scan_app_blueprint.route('/scan_app/signal_start', methods=["POST"])
def run_all_apps():
    if request.method == "POST":
        uid = request.get("uid")

        ###############################################################################
        #                        Post Request to story_distiller                      #
        ###############################################################################
        storydistiller_url = os.environ.get("STORYDISTILLER_URL")
        xbot_url = os.environ.get("XBOT_URL")
        owleye_url = os.environ.get("OWLEYE_URL")

        ###############################################################################
        #                    URL for storydistiller must be set up                    #
        ###############################################################################
        if storydistiller_url != None:
            story_distiler_api = storydistiller_url + "/" + signal_start_api_url

        else:
            warnings.warns("no url set for storydistiller in docker env")

        storydistiller_response = request.POST(storydistiller_url, data={"uid": uid})


        ###############################################################################
        #                          TODO: Do the same for xbot                         #
        ###############################################################################
        if xbot_url != None:
            xbot_api_api = xbot_url + "/" + signal_start_api_url
        else:
            warnings.warns("no url set for xbot in docker env")


        xbot_response = request.POST(xbot_url, data={"uid": uid})

        ###############################################################################
        #                          TODO: Do the same for owleye                       #
        ###############################################################################
        if owleye_url != None:
            owleye_api = owleye_url + "/" + signal_start_api_url

        owleye_response= request.POST(owleye_url, data={"uid": uid})

        ###############################################################################
        #                     Start polling for each and every app                    #
        ###############################################################################

# API which returns HTML file as response.
@app.websocket("/scan_app/image")
async def get(request: Request):
    ###############################################################################
    #                   TODO move this to results app if easier                   #
    ###############################################################################
    ###############################################################################
    #                     Once the websocket receives request update mongo db     #
    ###############################################################################
    mongo_db_file_id = request.get("file_id")

    # Assume the file is in bytes
    image_file = request.get("file_id")

    image_db = mongo.images


    # If the file is image
    im = Image.open("./image.jpg")
    image_bytes = io.BytesIO()

    im.save(image_bytes, format='JPEG')

    image = {
        'data': image_bytes.getvalue()
    }


    ###############################################################################
    #                              Add file to mongo                              #
    ###############################################################################
    # SOURCE: https://stackoverflow.com/questions/47668507/how-to-store-images-in-mongodb-through-pymongo
p
    dbResponse = db.files.insert_one(file)

    image_id = image_db.insert_one(image).inserted_id

@scan_app_blueprint.route('/redis_file_manager')
def home():
    return "Redis file manager is online"

