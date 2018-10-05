"""testing for orders"""
import unittest
import json


class TestOrders(unittest.TestCase):
    """ Tests for the Orders """
    def setUp(self):
        """setup"""
        app = create_app(config_name='testing')
        self.client = app.test_client()

        self.register_user = json.dumps(dict(
            username = "simon",
            email = "awitimon23@gmail.com",
            password ='Pass123',
            userRole='client',
            confirmpass='Pass123'))
        self.login = json.dumps(dict(username="useer", password='Pass123'))

        self.create_order = json.dumps(dict(
            order_id=1,
            description = 'kuku choma',
            status = "pending",
            address = 'CBD',
            deliveryTime = 'deliveryTime'))

        self.signupuser = self.client.post(
            '/v2/users/signup',
            data=self.register_user,
            content_type='application/json')

        self.client.post(
            '/v2/users/login',
            data=self.login,
            content_type='application/json')

        self.client.post(
            '/v2/users/orders',
            data=self.create_order,
            content_type='application/json')


    def test_order_creation(self):
        """ Test for order creation """
        resource = self.client.post(
            '/v2/users/orders',
            data=self.create_order,
            content_type='application/json')
        data = json.loads(resource.data.decode())
        self.assertEqual(resource.status_code, 201)
        self.assertEqual(resource.content_type, 'application/json')
        self.assertEqual(data['message'].strip(), 'Successful. Order created.')


    def test_get_all_orders(self):
        """ Test for getting all orders """
        resource = self.client.get(
            '/v2/orders/',
            data=json.dumps(dict()),
            content_type='application/json')
        data = json.loads(resource.data.decode())
        self.assertEqual(resource.status_code, 200)
        self.assertEqual(resource.content_type, 'application/json')
        self.assertEqual(data['message'].strip(), 'Successful. Orders Found.')

if __name__ == '__main__':
    unittest.main()