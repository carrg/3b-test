import unittest
from unittest.mock import patch
from flask import Flask
from src.routes.inventories import main as inventories_blueprint

class TestInventoriesRoutes(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(inventories_blueprint, url_prefix='/inventories')
        self.client = self.app.test_client()

    @patch('src.models.InventoryModel.InventoryModel.add_stock')
    def test_add_stock_success(self, mock_add_stock):
        mock_add_stock.return_value = 100
        response = self.client.patch('/inventories/product/1', json={'stock': 20})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': "Stock added successfully", 'stock': 100})

    @patch('src.models.InventoryModel.InventoryModel.add_stock')
    def test_add_stock_success(self, mock_add_stock):
        mock_add_stock.return_value = 0
        response = self.client.patch('/inventories/product/100', json={'stock': 20})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, {'message': "Product not found"})

    @patch('src.models.InventoryModel.InventoryModel.add_stock')
    def test_add_stock_success(self, mock_add_stock):
        mock_add_stock.return_value = -1
        response = self.client.patch('/inventories/product/100', json={'stock': 20})
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'message': "unexpected error"})

if __name__ == '__main__':
    unittest.main()