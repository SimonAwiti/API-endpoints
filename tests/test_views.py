from flask import  json, Flask
import unittest


app = Flask(__name__)

class Testendpoints(unittest.TestCase):


    def test_allorders(self):
        result = app.test_client()
        response= result.get('/api/v1/orders', content_type='application/json')
        self.assertTrue(response.status_code, 200)
    
    def test_postorder(self):
        result = app.test_client()
        response= result.post('/api/v1/orders',  content_type='application/json')
        self.assertTrue(response.status_code, 200)

    def test_updateorders(self):
        result = app.test_client()
        response= result.get('/api/v1/orders/3', content_type='application/json')
        self.assertTrue(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()