from flask import json, jsonify, abort, request
from data import MEALS

class MealsServer:
    def __init__(self):
        self.globalData = MEALS
from flask import Flask
app = Flask(__name__)

@app.route('/')
def getIndexPage():
    return "welcone to fastfood fast"

@app.route('/api/v2/meals', methods=['POST'] )
def add_new_meal():
    meal = {
        'id': MEALS[-1]['id'] + 1,
        'meal category': request.json['meal category']
    }
    MEALS.append(meal)
    return jsonify({'message': 'List of all meals', "meals":MEALS})

@app.route('/api/v2/meals', methods=['GET'])   
def get_list_of_meals():
    return jsonify ({'message':'List of all meals', "meals":MEALS})




   




