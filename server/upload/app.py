from flask import Blueprint, request
from redis import Redis, StrictRedis
from werkzeug.utils import secure_filename
from flask_cors import cross_origin
from werkzeug.datastructures import  FileStorage
import warnings
import linecache
import json
import codecs
import json
import zlib
import uuid
import pickle
import os

upload_blueprint = Blueprint("upload", __name__)
# r = Redis.from_url(os.environ.get('REDIS_URL'))
r = StrictRedis(decode_responses=True)

def unique_id_generator():
    res = "apk_file_" + str( uuid.uuid4() )
    return res


@upload_blueprint.route('/upload/apk', methods=["GET"])
def check_uploaded_apk_files():
    """
    This blueprint method acts as an api file uploader. It must be uploaded using form-data.
    The key in json for the apk file must be apk_file.
    """
    print("form", request.form)


    if request.method == "GET":
        redis_result = r.keys("apk_file*")
        print(redis_result)

        return json.dumps({"uploaded_apk_files": redis_result } ), 200

    return "no valid http request received", 200


@upload_blueprint.route('/upload/apk', methods=["GET", "POST"])
def upload():
    """
    This blueprint method acts as an api file uploader. It must be uploaded using form-data.
    The key in json for the apk file must be apk_file.
    """
    print("upload start")
    if request.method == "POST":
        ###############################################################################
        #                        If post http request received                        #
        ###############################################################################
        print("print request")
        # print(str(dir( request )))
        # print(str(request.files()))
        # print(json.loads(request.get_json(), encoding='utf-8'))
        # print(json.loads(str(request.file, encoding='utf-8')))

        file = request.form.get('apk_file', "no file")
        if 'file' not in request.get_json():
            warnings.warn("No file is detected in POST request.")
        else:
            file = request.get_json()['file']
            ###############################################################################
            #                              Generate unique id                             #
            ###############################################################################

            for i in range(100):
                print(str( linecache.getline(file["path"], i) ))

            print(file)

            file_key = "apk_file_" + unique_id_generator()

            ###############################################################################
            #                   Compress and byte serialise the apk file                  #
            ###############################################################################
            r.set(file_key, zlib.compress(pickle.dumps(file)))
            # r.set(file_key, file)

            return json.dumps({"file_key": str( file_key ) } ), 200


    return "no request file received", 200

@upload_blueprint.route('/upload/apk')
def home():
    return "Upload Is Online"


@upload_blueprint.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    header['Access-Control-Allow-Headers'] = '*'
    header['Access-Control-Allow-Methods'] = '*'
    # response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,timeout')
    # Other headers can be added here if needed
    # response.headers.add('Access-Control-Allow-Origin', '*')
    # response.headers.add('access-control-allow-headers', 'Content-Type')
    # response.headers.add('access-control-allow-headers', 'authorization')
    # response.headers.add('Access-Control-Allow-Methods', 'POST')
    return response

if __name__ == "__main__":
    print(unique_id_generator())
    print(unique_id_generator())
    print(unique_id_generator())
    print(unique_id_generator())
