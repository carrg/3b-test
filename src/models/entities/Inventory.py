
class Inventory():

    def __init__(self, id=None, product_id=None, stock=None, price=None) -> None:
        self.id = id
        self.product_id = product_id
        self.stock = stock
        self.price = price

    def to_JSON(self):
        return {
            'id': self.id,
            'product_id': self.product_id,
            'stock': self.stock,
            'price': self.price
        }
