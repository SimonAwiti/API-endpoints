import json, unittest
from flask import Flask

# from app.v1api.views import app
app = Flask(__name__)

class Testendpoints(unittest.TestCase):
    def test_allorders(self):
        result = app.test_client()
        response = result.get('/api/v1/orders', content_type='application/json')
        self.assertTrue(response.status_code, 200)
    
    def test_postorder(self):
        result = app.test_client()
        data = {
            "status": "Delivered",
            "deliveryTime": "1700",
            "address": "Kayole",
            "description": "Kuku Fry"
        }
        response = result.post('/api/v1/orders', data=json.dumps(data), content_type='application/json')
        self.assertTrue(response.status_code, 200)

    def test_updateorders(self):
        result = app.test_client()
        response = result.get('/api/v1/orders/2', content_type='application/json')
        self.assertTrue(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()