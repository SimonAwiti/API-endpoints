import os
from flask import Flask
from instance.config import app_config
from app.v2api.models.connectdb import initializedb

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    return app



