from flask import Flask
from .routes import products, inventories, orders
from flask_cors import CORS

app = Flask(__name__)
CORS(app=app, resources={r"*": {"origins": "*"}})

def init_app(config):
    """Main application function."""
    app.config.from_object(config)

    app.register_blueprint(products.main, url_prefix='/api/products')
    app.register_blueprint(inventories.main, url_prefix='/api/inventories')
    app.register_blueprint(orders.main, url_prefix='/api/orders')

    return app