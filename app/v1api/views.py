from flask import Flask, json, jsonify, abort, request
from data import orders
from data import orders
app=Flask(__name__)


@app.route('/', methods=['GET'])
def index_page():
    return  "welcone to fastfood fast"

@app.route('/api/v1/orders', methods=['POST'])
def add_new_order():
    order = {
        'id': orders[-1]['id'] + 1,
        'description': request.json['description'],
        'status': request.json['status'],
        'address': request.json['address'],
        'deliveryTime': request.json['deliveryTime']
   
    }
    orders.append(order)
    return jsonify({'order': order})

@app.route('/api/v1/orders', methods=['GET'])
def get_all_orders():
    return jsonify ({'orders':orders})

@app.route('/api/v1/orders/<int:Id>', methods=['GET'])
def get_order(Id):
    order = [order for order in orders if order['id'] == Id]
    if len(order) == 0:
        abort(404)
    return jsonify({'order': order[0]})

@app.route('/api/v1/orders/<int:Id>', methods=['PUT'])
def update_order(Id):
    order = [order for order in orders if order['id'] == Id]
    if len(order) == 0:
        abort(404)
    if not request.json:
        abort(400)


    return jsonify({'order': order[0]})



