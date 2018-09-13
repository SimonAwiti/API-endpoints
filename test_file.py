import getgenorders
import postorder
import putorder
def test_get_one_order():
    orders = get_one_order(orders[1])
    assert orders == 1
def test_get_all_orders():
    orders = get_all_orders(1)
    assert orders == ()  
def test_post_order():
    new_index = len(orders) + 1
    orders[new_index] = [data['1/1/2019'], data['2 piece chicken'], data['ksh 200'], data['spicy']]
    assert new_index == orders + [data['1/1/2019'], data['2 piece chicken'], data['ksh 200'], data['spicy']]
def test_update_orders():

     orders[ids] = [data['1/1/2019'], data['2 piece chicken'], data['ksh 200'], data['spicy']]
     assert orders == dorders + [data['1/1/2019'], data['2 piece chicken'], data['ksh 200'], data['spicy']], 202
