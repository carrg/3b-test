from flask import Blueprint, jsonify, request
from flask_cors import CORS
from src.models.OrderModel import OrderModel
from src.models.entities.Order import Order

main = Blueprint('orders_blueprint', __name__)
CORS(main)

@main.route('/', methods=['POST'])
def add_order():
    try:
        order_create = request.json

        order = OrderModel.create_order(order_create)
    
        if order > 0:
            return jsonify({'message': "Order created successfully", 'order': order}), 200
        else:
            return jsonify({'message': "unexpected error"}), 500
    
    except Exception as ex:
        print(str(ex))
        return jsonify({'message': "unexpected error"}), 500
