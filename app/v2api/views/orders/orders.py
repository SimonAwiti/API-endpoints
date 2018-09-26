from flask import Flask, request, flash, redirect, url_for, jsonify, session
from app.v2api.models.ordersmodels import Order
from app.v2api.views.orders.validateorders import validate_orders

orderObject = Order()
ordersapp
app = Flask(__name__)

@app.route('/api/v2/orders', methods=['POST'])
def order():
    """ Place an order for food."""
    data = request.get_json()
    resp = validate_orders(data)
    if resp == "valid":
        food_id = data['food_id']
        description = data['description']
        status = "pending"
        address = data['address']
        deliveryTime = data['deliveryTime']
        resp = orderObject.create_order(
            food_id,
            description,
            status,
            address,
            deliveryTime)
        return resp
    return jsonify({"message": resp}), 400

@app.route('/api/v2/orders', methods=['GET'])
def get_all_orders():
    """ Get all orders"""
    data = orderObject.get_orders()
    return data

@app.route('/api/v2/orders/<int:order_id>', methods=['GET', 'PUT'])
def order_editing(order_id, **kwargs):
    """ getting and editing an order """

    if request.method == 'PUT':
        ''''PUT Update the status  of an order'''
        data = request.get_json()
        food_id = data['food_id']
        description = data['description']
        status = data['status']
        address = data['address']
        deliveryTime = data['deliveryTime']
        resp = orderObject.update_order(
            order_id,
            description,
            status,
            address,
            deliveryTime)
        return resp
    else:
        ''''gets a specific order'''
        resp = orderObject.get_order(order_id)
        return resp


#@app.route('/api/v2/orders/<int:Id>', methods=['GET'])
#def userorders(client_id, **kwargs):
    """ Get the order history for a particular user."""
    #resp = orderObject.get_user_orders(client_id)
    #return resp