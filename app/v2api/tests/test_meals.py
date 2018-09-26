from flask import  json, Flask
import unittest


app = Flask(__name__)

class Testmealsendpoints(unittest.TestCase):


    def test_getmenu(self):
        result = app.test_client()
        response= result.get('/api/v2/menu', content_type='application/json')
        self.assertTrue(response.status_code, 200)

    def test_updatemenu(self):
        result = app.test_client()
        response= result.get('/api/v2/menu/3', content_type='application/json')
        self.assertTrue(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()