from src.database.db_mysql import get_connection

class OrderModel():
        
    @classmethod
    def create_order(self, order):
        try:
            connection = get_connection()

            total_price = sum((item['amount'] * item['price']) for item in order)

            with connection.cursor() as cursor:

                cursor.execute("""INSERT INTO orders (total) 
                                VALUES (%s)""", (total_price))
                affected_rows = cursor.rowcount

                if affected_rows == 1:
                    order_id = cursor.lastrowid

                    for item in order:
                        cursor.execute("""UPDATE inventories SET stock = stock - %s
                                WHERE product_id = %s""", (item['amount'], item['product_id']))
                        
                        cursor.execute("""INSERT INTO products_orders (product_id, order_id, amount, subtotal) 
                                    VALUES (%s, %s, %s, %s)""", (item['product_id'], order_id, item['amount'], item['amount'] * item['price']))
                        affected_rows = cursor.rowcount

                connection.commit()

            connection.close()
            return order_id

        except Exception as ex:
            raise Exception(ex)
        