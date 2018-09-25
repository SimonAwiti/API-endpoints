
'''app route the launches the server'''
from flask import Flask
from app import app
from app.v1api.views import app
from app.v1api import views




if __name__=='__main__':
    app.run(debug=True)