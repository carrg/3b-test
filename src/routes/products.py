from flask import Blueprint, jsonify, request
from flask_cors import CORS
from src.models.ProductModel import ProductModel
from src.models.entities.Product import Product
from decouple import config

main = Blueprint('products_blueprint', __name__)
CORS(main)

@main.route('/')
def get_products():
    try:
        products = ProductModel.get_products()
        return jsonify(products)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/create', methods=['POST'])
def create():
    name = request.json['name']
    sku = request.json['sku']
    price = request.json['price']

    product = Product(None, name, sku, price, config('STOCK_DEFAULT'))
    state = ProductModel.create_product(product)
    
    if state == 1:
        return jsonify({'message': "Product created successfully"}), 200
    elif state == 0:
        return jsonify({'message': "Product already exists"}), 409
    else:
        return jsonify({'message': "unexpected error"}), 500