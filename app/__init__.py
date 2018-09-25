from flask import Flask

app = Flask(__name__)

from app.v1api import views 