from app import app, orders
from flask import jsonify
# import ast

@app.route('/api/v1/orders', methods=['POST'])
def post_order():
   # print(dir(request))
   data = request.get_json()
   # data=data.decode("utf-8")
   # print(data)
   # data=ast.literal_eval(data)
   new_index = len(orders) + 1
   # print(len(data))
   orders[new_index] = [data['date'], data['description'], data['price'], data['status']]
   return jsonify({'data': orders[new_index]}), 201
