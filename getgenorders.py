from app import app, orders
from flask import jsonify
# import ast

@app.route('/api/v1/orders/<string:ids>')
def get_one_order(ids):
    return jsonify({'order':orders[ids]}) 

@app.route('/api/v1/orders')
def get_all_orders():
    return jsonify({'orders':orders})