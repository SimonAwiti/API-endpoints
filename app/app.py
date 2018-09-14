from flask import Flask, request
from flask import jsonify, request
import json
import requests
# import ast
app = Flask(__name__)

orders = {}