
'''app route the launches the server'''
from flask import Flask
from app import app
from app.v1api.views import app
#from app.v1api.views import views
#from app.v2api.orders import app
#from app.v2api.meals import app
from app.v1api import views
if __name__=='__main__':
    app.run(debug=True)