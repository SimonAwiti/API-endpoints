"""creating users routes"""
from flask import Blueprint, request, jsonify, session
from app.v2api.models.usersmodels import User
from app.v2api.views.users.validateusers import validate_data_signup, validate_data_login

v2API_auth_blueprints = Blueprint('v2API_auth', __name__, url_prefix='/api/v2/users')

userObject = User()

@v2API_auth_blueprints.route('/signup', methods=["POST"])
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

@v2API_auth_blueprints.route('/login', methods=["POST"])
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

@v2API_auth_blueprints.route('/logout')
def logout():
    """ logout user."""
    if 'username' in session:
        session.clear()
        return jsonify({"message": "Succeffully logout."})
    return jsonify({
        "message": "Not logged in."}), 200
        