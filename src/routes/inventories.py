from flask import Blueprint, jsonify, request
from flask_cors import CORS
from src.models.InventoryModel import InventoryModel
from src.models.entities.Inventory import Inventory

main = Blueprint('inventories_blueprint', __name__)
CORS(main)

@main.route('/product/<id>', methods=['PATCH'])
def add_stock(id):
    try:
        stock = request.json['stock']

        inventory = Inventory(None, product_id=id, stock=stock, price=None)
        stock = InventoryModel.add_stock(inventory)
    
        if stock == 0:
            return jsonify({'message': "Product not found"}), 404
        elif stock > 0:
            return jsonify({'message': "Stock added successfully", 'stock': stock}), 200
        else:
            return jsonify({'message': "unexpected error"}), 500
    
    except Exception as ex:
        print(str(ex))
        return jsonify({'message': "unexpected error"}), 500
