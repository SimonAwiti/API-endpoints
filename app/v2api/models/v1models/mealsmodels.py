from flask import jsonify, session
import re 

class Meal(object):
    def __init__(self):
        """ Initialize empty Order list"""
        self.meal_list = []
        self.notfound = None

    def create_meal(self, meal_id, mealcategory):
        """Create food_item"""
        self.meal = {}
        if self.is_loggedin() is True:
            if self.is_admin() is True:
                self.mealId = len(self.meal_list)
                self.meal['meal_id'] = self.meal_id + 1
                self.meal['mealcategory'] = mealcategory
                self.meal_list.append(self.meal)
                return jsonify({
                    "message": "Successful.",
                    "Meal": self.meal_list}), 201
            return jsonify({
                "message": "You dont administrator priviledges."}), 401
        return jsonify({
            "message": "Please login first."}), 401

    def get_meal(self):
        """ get all meals """
        if len(self.meal_list) > 0:
            return jsonify({
                "message": "Successful.",
                "Meals": self.meal_list}), 200
        return jsonify({
            "message": "No meals found."}), 400


    