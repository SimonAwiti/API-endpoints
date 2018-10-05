"""creating orders"""
from flask import jsonify, session
import re 

class Order(object):
    def __init__(self):
        """ Initialize empty Order list"""
        self.order_list = []
        self.notfound = None

    def create_order(self, order_id, description, status, address, deliveryTime):
        """Creating orders"""
        self.orders = {}
        if self.is_loggedin() is True:
            self.orderId = len(self.order_list)
            self.orders['food_id'] = food_id
            self.orders['description'] = description
            self.orders['status'] = status
            self.orders['address'] = address
            self.orders['deliveryTime'] = deliveryTime
            self.orders['order_id'] = self.orderId + 1
            self.order_list.append(self.orders)
            return jsonify({
                "message": "Successful.",
                "Orders": self.order_list}), 201
        return jsonify({
            "message": "Please login first."}), 401

    def get_orders(self):
        """ getting all Orders """
        if self.is_loggedin() is True:
            if self.is_admin() is True:
                if len(self.order_list) > 0:
                    return jsonify({
                     "message": "Successful.",
                     "Order": self.order_list}), 200
                return jsonify({
                    "message": "No any available order."}), 404
            return jsonify({
                "message": "You dont have administrator priviledges."}), 403
        return jsonify({
            "message": "Please login first."}), 401

    def update_order(
            self,
            order_id,
            description,
            status,
            address,
            deliveryTime):
        """ update Order """
        if self.is_loggedin() is True:
            if self.is_admin() is True:
                if len(self.order_list) > 0:
                    for order in self.order_list:
                        if order['order_id'] == order_id:
                            order['description'] = description
                            order['status'] = status
                            order['address'] = address
                            order['deliveryTime'] = deliveryTime
                            return jsonify({
                                "message": "Update Successful.",
                                "Orders": self.order_list}), 201
                        self.notfound = True
                    if self.notfound is True:
                        return jsonify({
                            "message": "No order with provided id."}), 404
                return jsonify({
                    "message": "No order."}), 400
            return jsonify({
                "message": "You dont have administrator priviledges."}), 403
        return jsonify({
            "message": "Please login first."}), 401

    def get_order(self, order_id):
        """ get Order """
        if self.is_loggedin() is True:
            if self.is_admin() is True:
                if len(self.order_list) > 0:
                    for order in self.order_list:
                        if order['order_id'] == order_id:
                            return jsonify({
                                "message": "Successful.",
                                "Order": order}), 200
                        self.notfound = True

                    if self.notfound is True:
                        return jsonify({
                            "message": "No order with that id."}), 404
                return jsonify({
                    "message": "No order."}), 404
            return jsonify({
                "message": "You dont have administrator priviledges."}), 403
        return jsonify({
            "message": "Please login first."}), 401

    def is_loggedin(self):
        if 'username' in session:
            if session['username']:
                return True
        return False

    def is_admin(self):
        if 'userrole' in session:
            if session['userrole'] == 'admin':
                return True
        return False
