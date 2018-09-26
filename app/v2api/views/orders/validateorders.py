def validate_orders(data):
    """validate orders details"""
    try:
        # check if food_id is empty
        if data["food_id"] is False:
            return "food_id required"
        #check description is empty
        elif data["description"] is False:
            return "description required"
        #check if status is empty
        elif data["status"] is False:
            return "status required"
        # check if address is empty
        elif data["address"] is False:
            return "address required"
        else:
            return "valid"
    except Exception as error:
        return "please provide all the fields, missing " + str(error)