from flask import Flask, request
from flask import jsonify
import json
import requests
import ast


app = Flask(__name__)



orders = {}

@app.route('/api/v1/orders')
def get_all_orders():
    return jsonify({'orders':orders})





if __name__ == '__main__':
    app.run()
