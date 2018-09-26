from flask import Flask

app = Flask(__name__)

from app.v2api import orders, meals, users