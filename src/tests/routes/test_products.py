import unittest
from unittest.mock import patch
from flask import Flask
from src.routes.products import main as products_blueprint

class TestProductsRoutes(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(products_blueprint, url_prefix='/products')
        self.client = self.app.test_client()

    @patch('src.models.ProductModel.ProductModel.get_products')
    def test_get_products(self, mock_get_products):
        mock_get_products.return_value = [{'id': 1, 'name': 'Test Product', 'sku': 'SKU', 'price': 10.99, 'stock': 100}]
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [{'id': 1, 'name': 'Test Product', 'sku': 'SKU', 'price': 10.99, 'stock': 100}])

    @patch('src.models.ProductModel.ProductModel.create_product')
    def test_create_product_new(self, mock_create_product):
        mock_create_product.return_value = 1
        response = self.client.post('/products/create', json={'name': 'New Product', 'sku': 'SKU123', 'price': 10.99})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': "Product created successfully"})

    @patch('src.models.ProductModel.ProductModel.create_product')
    def test_create_product_exists(self, mock_create_product):
        mock_create_product.return_value = 0
        response = self.client.post('/products/create', json={'name': 'Existing Product', 'sku': 'SKU123', 'price': 10.99})
        self.assertEqual(response.status_code, 409)
        self.assertEqual(response.json, {'message': "Product already exists"})

if __name__ == '__main__':
    unittest.main()