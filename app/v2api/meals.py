from flask import Flask, json, jsonify, abort, request
from data2 import meals
app=Flask(__name__)



@app.route('/api/v2/menu', methods=['GET'])   
def get_menu():
    return jsonify ({'meals':meals})


@app.route('/api/v2/menu/<int:id>', methods=['PUT'])
def update_menu_status(id):
    meal = [ meal for meal in meals if meal['id'] == id]
    meal[0]['id'] = request.json.get('id', meal[0]['id'])
    meal[0]['meal category'] = request.json.get('meal category', meal[0]['meal category'])
    return jsonify({'meal':meal[0]})