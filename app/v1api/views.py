from flask import Flask, json, jsonify, abort, request
from data import ORDERS
app = Flask(__name__)

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
    ORDERS.append(order)
    return jsonify({'message': 'Order placed succesfully', "orders":order})
    
@app.route('/api/v1/orders', methods=['GET'])
def get_all_orders():
    return jsonify({'message': 'List of all placed orders', "orders":ORDERS})

@app.route('/api/v1/orders/<int:Id>', methods=['GET'])
def get_order(Id):
    order = [order for order in ORDERS if order['id'] == Id]
    if len(order) == 0:
        abort(404)
    return jsonify({'message': 'Order as per your id', "orders":order})

@app.route('/api/v1/orders/<int:id>', methods=['PUT'])
def update_order_status(id):
    order = [order for order in ORDERS if order['id'] == id]
    if not order:
        return jsonify({"message": "The order with id %s does not exist"%id})
    order[0]['id'] = request.json.get('id', order[0]['id'])
    status = request.json.get('status', None)
    if not status:
        return jsonify({"message": "provide status"})
    if str(status) not in (["delivered", "pending"]):
        return jsonify(
            {'Messaage':'status should eirther be pending or delivered', "order":order[0]}
            )
    order[0]['status'] = request.json.get('status', order[0]['status'])
    return jsonify({'message':'Order edited succesfully', "order":order})
   


