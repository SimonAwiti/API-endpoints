from flask import jsonify, session
import re
from 
class User(object):
    def __init__(self):
        '''begin with an empty list'''
        self.users_list = []
        self.notfound = None 

    def create_user(self, username, password, email):
        """Creating users"""
        self.users = {}
        if not self.valid_username(username):

            self.id = len(self.users_list)
            self.users['username'] = username
            self.users['password'] = password
            self.users['email'] = email
            self.users['userid'] = self.id + 1
            self.users_list.append(self.users)

                        
            userlistclone = {}
            for user in self.users_list:
                if user['userid'] == self.users['userid']:
                    '''ommit password from response'''
                    userlistclone.update({
                        'user_id': user['userid'],
                        'username': user['username'],
                        'email': user['email']})
            return jsonify({"message": "Successful", "user": userlistclone}), 201
        return jsonify({"message": "Username is added."}), 400

    def login(self, username, password):
        """login users"""
        if len(self.users_list) == 0:
            return jsonify({"message": "Please register first."}), 400
        else:
            userlistclone = {}
            for user in self.users_list:
                if username == user['username']:
                    if password == user['password']:
                        session['userid'] = user['userid']
                        session['username'] = user['username']
                        '''ommit password from response'''
                        userlistclone.update({
                            'user_id': user['userid'],
                            'username': user['username'],
                            'email': user['email']})
                        return jsonify({
                            "message": "You are successfully logged in",
                            "user": userlistclone}), 200
                    else:
                        return jsonify({
                            "message": "Wrong username or password"}), 401
                else:
                    self.notfound = True
            if self.notfound is True:
                return jsonify({"message": "user does not exist"}), 400

    def get_users(self):
        """get all user """
        userlistclone = {}
        result = []
        if len(self.users_list) > 0:
            for user in self.users_list:
                '''ommit password from response'''
                userlistclone.update({
                    'user_id': user['userid'],
                    'username': user['username'],
                    'email': user['email']})
                result.append(dict(userlistclone))
            return jsonify({
                "message": "Successful.",
                "Users": result}), 200
        return jsonify({
            "message": "No user."}), 400

    def update_user(
            self,
            id,
            username,
            email,
            password):
        """ update User """

        userlistclone = {}
        if len(self.user_list) > 0:
            for user in self.users_list:
                if user['userid'] == id:
                    user['username'] = username
                    user['email'] = email
                    user['password'] = password
                    '''ommit password from result'''
                    userlistclone.update({
                        'user_id': user['userid'],
                        'username': user['username'],
                        'email': user['email']})
                    return jsonify({
                        "message": "Update Successful.",
                        "Users": userlistclone}), 201
                self.notfound = True
            if self.notfound is True:
                return jsonify({
                    "message": "User doesn't exist."}), 400
        return jsonify({
            "message": "No user."}), 400    

    def valid_username(self, username):
        """check if username exist"""
        if len(self.users_list) > 0:
            for user in self.users_list:
                if user['username'] == username:
                    return True
                self.notfound = True
            if self.notfound is True:
                    return False
        return False

    def valid_password(self, password):
        """check password length and special characters"""
        if len(password) < 3 or not re.match("^[a-zA-Z0-9_ ]*$", password):
            return False
        else:
            return True

