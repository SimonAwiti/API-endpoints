from flask import request, flash, redirect, url_for, jsonify, session
from app.v2api.models.usersmodels import User
from app.v2api.views.users.validateusers import validate_data_signup, validate_data_login



from flask import Flask
app = Flask(__name__)

userObject = User()

@app.route('/users/signup', methods=["POST"])
def register():
    """creating user account."""
    data = request.get_json()
    resp = validate_data_signup(data)

    if resp == "valid":
        username = data['username']
        email = data['email']
        password = data['password']
        response = userObject.create_user(
            username,
            email,
            password)
        return response
    return jsonify({"message": resp}), 400

@app.route('/users/login', methods=["POST"])
def login():
    """ loging in user """
    data = request.get_json()
    resp = validate_data_login(data)
    if resp == "valid":
        username = data['username']
        password = data['password']
        resp = userObject.login(username, password)
        return resp
    return jsonify({"message": resp}), 401

@app.route('/users', methods=["GET"])
def users():
    data = userObject.get_users()
    return data

@app.route('/users/logout')
def logout():
    """ logout user."""
    if 'username' in session:
        session.clear()
        return jsonify({"message": "Succeffully logout."})
    return jsonify({
        "message": "Not logged in."}), 200