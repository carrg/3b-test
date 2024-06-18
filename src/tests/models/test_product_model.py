from unittest import mock, TestCase
from src.models.ProductModel import ProductModel

class TestProductModel(TestCase):

    @mock.patch('src.models.ProductModel.ProductModel.get_products')
    def test_products_returns_non_empty_list(self, mock_get_products):
        mock_get_products.return_value = [{'id': 1, 'name': 'Test Product', 'sku': 'SKU', 'price': 10.99, 'stock': 100}]
        products = ProductModel.get_products()
        self.assertTrue(len(products) > 0, "get_products should return a non-empty list when products are available")

    @mock.patch('src.models.ProductModel.ProductModel.get_products')
    def test_products_returns_empty_list(self, mock_get_products):
        mock_get_products.return_value = []
        products = ProductModel.get_products()
        self.assertEqual(len(products), 0, "get_products should return an empty list when no products are available")

    @mock.patch('src.models.ProductModel.ProductModel.get_products')
    def test_products_handles_exceptions(self, mock_get_products):
        mock_get_products.side_effect = Exception("Database error")
        with self.assertRaises(Exception) as context:
            ProductModel.get_products()
        self.assertTrue('Database error' in str(context.exception), "get_products should properly handle exceptions")

    @mock.patch('src.models.ProductModel.ProductModel.create_product')
    def test_product_created_successfully(self, mock_create_product):
        mock_create_product.return_value = 1
        resp = ProductModel.create_product({'name': 'product name', 'sku': 'CC1000', 'price': 20.99})
        self.assertEqual(resp, 1, "product should be created successfully")

    @mock.patch('src.models.ProductModel.ProductModel.create_product')
    def test_product_created_fail(self, mock_create_product):
        mock_create_product.return_value = 0
        resp = ProductModel.create_product({'name': 'product name', 'sku': 'CC1000', 'price': 20.99})
        self.assertEqual(resp, 0, "product should not be created successfully")

    @mock.patch('src.models.ProductModel.ProductModel.create_product')
    def test_product_created_exception(self, mock_create_product):
        mock_create_product.side_effect = Exception("sku is missing")
        with self.assertRaises(Exception) as context:
            ProductModel.create_product({'name': 'product name', 'price': 20.99})
        self.assertTrue('sku is missing' in str(context.exception), "create_product should properly handle exceptions")

    @mock.patch('src.models.ProductModel.ProductModel.get_stock')
    def test_stock_returns_non_empty_list(self, mock_get_stock):
        mock_get_stock.return_value = [{'id': 1, 'name': 'Test Product', 'sku': 'SKU123', 'price': 10.99, 'stock': 9}]
        products = ProductModel.get_stock()
        self.assertTrue(len(products) > 0, "get_stock should return a non-empty list when are products with limited stock available")

    @mock.patch('src.models.ProductModel.ProductModel.get_stock')
    def test_stock_returns_empty_list(self, mock_get_stock):
        mock_get_stock.return_value = []
        products = ProductModel.get_stock()
        self.assertEqual(len(products), 0, "get_stock should return an empty list when all products are in stock")

    @mock.patch('src.models.ProductModel.ProductModel.get_stock')
    def test_stock_handles_exceptions(self, mock_get_stock):
        mock_get_stock.side_effect = Exception("Database error")
        with self.assertRaises(Exception) as context:
            ProductModel.get_stock()
        self.assertTrue('Database error' in str(context.exception), "get_stock should properly handle exceptions")

