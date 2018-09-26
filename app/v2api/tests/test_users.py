from flask import  json, Flask
import unittest


app = Flask(__name__)

class Testuserendpoints(unittest.TestCase):
    def test_user(self):
        result = app.test_client()
        response= result.get('/api/v2/user/2', content_type='application/json')
        self.assertTrue(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()