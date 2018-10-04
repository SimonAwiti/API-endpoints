ef validate_meals(data):
    """validate meals details"""
    try:
        # check if meal category is empty
        if data["mealcategory"] is False:
            return "mealcategory required"
        else:
            return "valid"
    except Exception as error:
        return "please provide all the fields, missing " + str(error)
