"""models file for the app"""
import re
import jwt
import datetime
from flask import jsonify, session
from app.v2api.db.connectdb import dbconnect

def is_admin():
    """ check if a user is an admin """
    if 'token' in session:
        token = session['token']
        token = jwt.decode(token, 'SECRET_KEY', algorithms=['HS256'])
        if token['userRole'] == 'admin':
            return True
    return False


class User(object):
    """User Class"""

    def __init__(self):
        """ Initialize with an empty user list"""
        self.connect = dbconnect()
        self.cur = self.connect.cursor()
        self.users = {}
        self.userlist = {}
        self.result = []

    def create_user(self, username, email, password, userRole):
        """Create users"""
        if not self.valid_username(username):
            if not self.valid_email(email):
                self.cur.execute(
                        "INSERT INTO users(username, email, password, userRole) VALUES(%s, %s, %s,%s);", (
                         username, email, password, userRole))
                self.connect.commit()
                return jsonify({"message": "Registration Successful"}), 201
        else:
            return jsonify({"message": "Username or Email already in use."}), 400

    def login(self, username, password):
        """login users"""
        if not self.valid_username(username):
            return jsonify({"message": "Please register first."}), 401
        self.cur.execute("SELECT * FROM users WHERE username='%s'\
        AND password='%s'"%username, password)
        if self.cur.rowcount > 0:
            rows = self.cur.fetchall()
            for user in rows:
                user_id = user[0]
                username = user[1]
                email = user[4]
                userRole = user[5]
                session['token'] = jwt.encode({'userid': user_id,
                                               'username': username, 'userrole': userRole,
                                               'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
                                              'SECRET_KEY', algorithm='HS256')
                return jsonify({
                    "message": "You are successfully logged in"}), 200
        return jsonify({
            "message": "Wrong username or password"}), 403
    def valid_username(self, username):
        """check if username exist"""
        self.cur.execute("SELECT * FROM users WHERE username='%s'"%username)
        numrows = self.cur.rowcount
        if numrows > 0:
            return True
        return False

    def valid_email(self, email):
        """check if email exist"""
        self.cur.execute("SELECT * FROM users WHERE email='%s'"%email)
        numrows = self.cur.rowcount
        if numrows > 0:
            return True
        return False
    
class Order(object):
    """orders class"""

    def __init__(self):
        """ Initialize empty Order list"""
        self.conn = dbconnect()
        self.cur = self.conn.cursor()
        self.orderlist = {}
        self.result = []

    def create_order(order_id, description, status, address, deliverTime):
        """Create order_item"""
        self.cur.execute("INSERT INTO users(order_id, description, status, address, deliveryTime) VALUES(%s, %s, %s,%s);", (
                        order_id, description, status, address, deliverTime))
        self.conn.commit()
        return jsonify({"message": "Successful. Order created."}), 201
    
    def get_orders(self):
        """ get all Orders """
        if is_admin() is True:
            self.cur.execute("SELECT * FROM orders")
            if self.cur.rowcount > 0:
                rows = self.cur.fetchall()
                for order in rows:
                    self.orderlist.update({
                        'order_id': order[0],
                        'description': order[1],
                        'status': order[2],
                        'address': order[3],
                        'deliveryTime': order[4]})
                    self.result.append(dict(self.orderlist))
                return jsonify({
                    "message": "Successful. Orders Found.",
                    "Orders": self.result}), 200
            return jsonify({
                "message": "No Order."}), 400
        return jsonify({
            "message": "You dont have admin priviledges."}), 401
        
    def get_order(self, order_id):
        """ get Order """
        if is_admin() is True:
            self.cur.execute("SELECT * FROM orders WHERE order_id='%s'"%order_id)
            if self.cur.rowcount > 0:
                rows = self.cur.fetchall()
                for order in rows:
                    self.orderlist.update({
                        'order_id': order[0],
                        'description': order[1],
                        'status': order[2],
                        'address': order[3],
                        'deliveryTime': order[4]})
                    self.result.append(dict(self.orderlist))
                return jsonify({
                    "message": "Successful. Order found.",
                    "Orders": self.result}), 200
            return jsonify({
                "message": "No Order."}), 400
        return jsonify({
            "message": "You dont have admin priviledges."}), 401

    def update_order(
            self,
            order_id,
            description,
            status,
            address,
            deliveryTime):
        """ update Order """
        if is_admin() is True:
            self.cur.execute("SELECT * FROM orders WHERE order_id='%s'"%order_id)
            rows = self.cur.fetchall()
            if self.cur.rowcount > 0:
                # update this order details
                self.cur.execute(
                    "UPDATE orders SET order_id=%s, description=%s,\
                status=%s, address=%s, deliveryTime=%s WHERE order_id=%s",
                    (order_id,
                     description,
                     status,
                     address,
                     deliveryTime))
                self.conn.commit()

                for order in rows:
                    self.orderlist.update({
                        'order_id': order[0],
                        'description': order[1],
                        'status': order[2],
                        'address': order[3],
                        'deliveryTime': order[4]})
                    return jsonify({
                        "message": "Update Successful.",
                        "Order": self.orderlist}), 201
            return jsonify({"message": "No Order."}), 400
        return jsonify({
            "message": "You dont have admin priviledges."}), 401


    
