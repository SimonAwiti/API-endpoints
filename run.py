
'''app route the launches the server'''
from flask import Flask
#from app import app
#from app.v2api.views.index import app
from app.v2api.views.orders.orders import app
#from app.v2api.views.users.users import app

#from app.v2api.views import meals


if __name__ == '__main__':
    app.run(debug=True)
