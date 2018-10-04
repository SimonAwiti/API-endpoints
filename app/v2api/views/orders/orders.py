"""creating bp routes for orders"""
from flask import Blueprint, request, jsonify
from app.v2api.models.ordersmodels import Order
from app.v2api.views.orders.validateorders import validate_orders

orderObject = Order()

v2API_blueprints = Blueprint('v2API', __name__, url_prefix='/api/v2/orders')

@v2API_blueprints.route('/', methods=['POST'])
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

@v2API_blueprints.route('/', methods=['GET'])
#""" Get all orders"""
def get_all_orders():
    data = orderObject.get_orders()
    return data

@v2API_blueprints.route('/<int:order_id>', methods=['GET', 'PUT'])
#""" getting and editing an order """
def order_editing(order_id, **kwargs):
    if request.method == 'PUT':
        #''''PUT Update the status  of an order'''
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
        #''''gets a specific order'''
        resp = orderObject.get_order(order_id)
        return resp
