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
    return jsonify({'Message: order posted succesfully to the orders list': order})

@app.route('/api/v1/orders', methods=['GET'])
def get_all_orders():
    return jsonify ({'Message: List of all placed orders':orders})

@app.route('/api/v1/orders/<int:Id>', methods=['GET'])
def get_order(Id):
    order = [order for order in orders if order['id'] == Id]
    if len(order) == 0:
        abort(404)
    return jsonify({'Message: Order as per your ID': order[0]})

@app.route('/api/v1/orders/<int:id>', methods=['PUT'])
def update_order_status(id):
    order = [ order for order in orders if order['id'] == id]
    order[0]['id'] = request.json.get('id', order[0]['id'])
    order[0]['status'] = request.json.get('status', order[0]['status'])
    #if order[0]['status'] is not json({'delivered'}):
        #return jsonify ({'message :order cannot be edited':order[0]})
    return jsonify({'Messaage:Order edited succesfully(note:status can only be delivered, pending or rejected':order[0]})
    #return jsonify ({'message':'order cannot be edited':order[0]})


