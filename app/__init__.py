#'''creating and initilizing app'''
import os
from flask import Flask
from instance.config import app_config
from app.v2api.models.connectdb import initializedb

        #'''creating the application'''
def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    
        #'''initializing the database'''
    initializedb()
 
        #'''importing and registering the blueprints'''
    from app.v2api.views.orders.orders import v2API_blueprints
    app.register_blueprint(v2API_blueprints)

    from app.v2api.views.users.users import v2API_auth_blueprints
    app.register_blueprint(v2API_auth_blueprints)

    return app
