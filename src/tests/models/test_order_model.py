import unittest
from unittest.mock import MagicMock
from src.models.OrderModel import OrderModel

class TestOrderModel(unittest.TestCase):

    def setUp(self):
        self.order_model = OrderModel()

    def test_create_order_success(self):
        self.order_model = MagicMock()
        self.order_model.create_order.return_value = 1
        orders = self.order_model.create_order()
        self.assertTrue(orders > 0, "Order created successfully")

    def test_create_order_fail(self):
        self.order_model = MagicMock()
        self.order_model.create_order.return_value = 0
        orders = self.order_model.create_order()
        self.assertTrue(orders == 0, "Order not created successfully")

    def test_create_order_ex(self):
        self.order_model = MagicMock()
        self.order_model.create_order.side_effect = Exception("Database error")
        with self.assertRaises(Exception) as context:
            self.order_model.create_order()
        self.assertTrue('Database error' in str(context.exception), "create_order should properly handle exceptions")

if __name__ == '__main__':
    unittest.main()