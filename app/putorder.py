from app import app, orders
from flask import jsonify, request
# import ast
       
@app.route('/api/v1/orders/<string:ids>', methods=['PUT'])
def  update_orders(ids):
    # import pdb;pdb.set_trace()
    data = request.get_json()
    # data=data.decode("utf-8")
    # data=ast.literal_eval(data)
    orders[ids] = [data['date'], data['description'], data['price'], data['status'], data['address'], data['deliveryTime']]
    return jsonify({'data': data}), 202
