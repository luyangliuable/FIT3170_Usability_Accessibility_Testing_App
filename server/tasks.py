from flask import jsonify, send_file
from celery import Celery
# from scan_app.app import *
import time
import os

celery = Celery(__name__)
celery.conf.broker_url = os.environ['REDIS_URL']
celery.conf.result_backend = os.environ['REDIS_URL']


@celery.task(name="create_task")
def create_task(info={}):
    ###############################################################################
    #                           Create celery web tasks                           #
    ###############################################################################

    # time.sleep(1)
    print("task completed")

    ###############################################################################
    #                              Start scanner_app                              #
    ###############################################################################

    result = {"files": ["file_url_placeholder"], "images": ["image_url_placeholder"]}

    return result, 200
