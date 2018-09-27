from flask import Flask, json, jsonify, abort, request
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

@app.route('/api/v1/orders/<int:id>', methods=['PUT'])
def update_order_status(id):
    order = [ order for order in orders if order['id'] == id]
    order[0]['id'] = request.json.get('id', order[0]['id'])
    order[0]['description'] = request.json.get('description', order[0]['description'])
    order[0]['status'] = request.json.get('status', order[0]['status'])
    order[0]['address'] = request.json.get('address', order[0]['address'])
    order[0]['deliveryTime'] = request.json.get('deliveryTime', order[0]['deliveryTime'])
    return jsonify({'order':order[0]})



