import unittest
#import pytest
#from app import app

#@pytest.fixture
#def client(request):
    #test_client = app.test_client()


def test_get_one_orders(client):
    response = client.get('/api/v1/orders/<string:ids>')
    assert response.status_code == 200

def test_post_order(client):
    response = client.post('api/v1/orders')
    assert response.status_code == 201
 

def test_update_orders(client):
    response = client.put('/api/v1/orders/<string:ids>')
    assert response.status_code == 202



