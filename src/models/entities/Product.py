
class Product():

    def __init__(self, id=None, name=None, sku=None, price=None, stock=None) -> None:
        self.id = id
        self.name = name
        self.sku = sku
        self.price = price
        self.stock = stock

    def to_JSON(self):
        return {
            'id': self.id,
            'name': self.name,
            'sku': self.sku,
            'price': self.price,
            'stock': self.stock
        }
