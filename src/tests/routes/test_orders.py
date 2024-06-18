import unittest
from unittest.mock import patch
from flask import Flask
from src.routes.orders import main as orders_blueprint

class TestOrdersRoutes(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(orders_blueprint, url_prefix='/orders')
        self.client = self.app.test_client()

    @patch('src.models.OrderModel.OrderModel.create_order')
    def test_create_order_success(self, mock_create_order):
        mock_create_order.return_value = 1
        response = self.client.post('/orders/', json={'product_id': 1, 'amount': 2, 'price': 20.5})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': "Order created successfully", "order": 1})

    @patch('src.models.OrderModel.OrderModel.create_order')
    def test_create_order_fail(self, mock_create_order):
        mock_create_order.return_value = 0
        response = self.client.post('/orders/', json={'product_id': 1, 'amount': 2, 'price': 20.5})
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'message': "unexpected error"})

if __name__ == '__main__':
    unittest.main()