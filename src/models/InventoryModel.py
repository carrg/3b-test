from src.database.db_mysql import get_connection

class InventoryModel():
        
    @classmethod
    def add_stock(self, inventory):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""SELECT id FROM products  
                                WHERE id = %s""", (inventory.product_id))
                row = cursor.fetchone()
                
                if row is None:
                    return 0
                
                product_id = row[0]
                cursor.execute("""UPDATE inventories SET stock = stock + %s
                                WHERE product_id = %s""", (inventory.stock, product_id))

                cursor.execute("""SELECT stock FROM inventories WHERE product_id = %s""", (product_id))
                row = cursor.fetchone()
                stock = row[0]

                connection.commit()

            connection.close()
            return stock

        except Exception as ex:
            raise Exception(ex)

        