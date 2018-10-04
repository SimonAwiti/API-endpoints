"""creating bp routes for meals
from flask import Blueprint, request, jsonify
from app.v2api.models.mealsmodels import Meal
from app.v2api.views.meals.validatemeals import validate_meals

instantiate class
mealObject = Meal()

v2API_menu_blueprints = Blueprint('v2API', __name__, url_prefix='/api/v2/')

@v2API_menu_blueprints.route('/menu', methods=["GET", "POST"])
def meals():
    Method to create and retrieve meal.
    if request.method == "POST":
        data = request.get_json()
        res = validate_data(data)
        if resp == "valid":
            mealcategory = data['mealcategory']
            res = mealObject.create_meal(mealscategory)
            return resp
        return jsonify({"message": res}), 400
    data = mealObject.get_meal()
    return data"""
