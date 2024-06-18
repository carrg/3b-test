
class Order():

    def __init__(self, id=None, product_id=None, price=None, amount=None) -> None:
        self.id = id
        self.product_id = product_id
        self.price = price
        self.amount = amount

    def to_JSON(self):
        return {
            'id': self.id,
            'product_id': self.product_id,
            'price': self.price,
            'amount': self.amount
        }
