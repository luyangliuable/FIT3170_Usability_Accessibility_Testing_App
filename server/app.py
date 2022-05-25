import os
from flask import Flask
from tasks import celery
from flask_cors import CORS

def create_app(script_info=None):

    # instantiate the app
    app = Flask(__name__)

    # set config
    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)

    # register blueprints
    from main.views import main_blueprint
    from upload.app import upload_blueprint
    from redis_file_manager.app import redis_file_manager_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(upload_blueprint)
    app.register_blueprint(redis_file_manager_blueprint)

    ###############################################################################
    #                              Enable debug mode                              #
    ###############################################################################
    app.config['DEBUG'] = True
    app.debug = True

    ###############################################################################
    #                                Upload folder                                #
    ###############################################################################
    app.config['UPLOAD_FOLDER'] = "./upload/files"

    ###############################################################################
    #                           Add cors to flask server                          #
    ###############################################################################
    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'

    # shell context for flask cli
    app.shell_context_processor({"app": app})


    return app
