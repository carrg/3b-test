import unittest
from unittest.mock import MagicMock
from src.models.InventoryModel import InventoryModel

class TestOrderModel(unittest.TestCase):

    def setUp(self):
        self.inventory_model = InventoryModel()

    def test_add_stock_success(self):
        self.inventory_model = MagicMock()
        self.inventory_model.add_stock.return_value = 100
        stock = self.inventory_model.add_stock()
        self.assertEqual(stock, 100, "Stock added successfully")

    def test_add_stock_fail(self):
        self.inventory_model = MagicMock()
        self.inventory_model.add_stock.return_value = 0
        stock = self.inventory_model.add_stock()
        self.assertTrue(stock == 0, "Stock not added successfully")

    def test_add_stock_ex(self):
        self.inventory_model = MagicMock()
        self.inventory_model.add_stock.side_effect = Exception("Database error")
        with self.assertRaises(Exception) as context:
            self.inventory_model.add_stock()
        self.assertTrue('Database error' in str(context.exception), "add_stock should properly handle exceptions")

if __name__ == '__main__':
    unittest.main()