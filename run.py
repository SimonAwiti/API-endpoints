#'''initilize the server'''
from os import getenv
from app import create_app

config_name = getenv('APP_SETTINGS')
app = create_app(config_name)

if __name__ == '__main__':
    app.run()
