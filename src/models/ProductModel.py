from src.database.db_mysql import get_connection
from .entities.Product import Product

class ProductModel():
    
    @classmethod
    def get_products(self):
        try:
            connection = get_connection()
            products = []

            with connection.cursor() as cursor:
                cursor.execute("""SELECT a.id, a.name, a.sku, b.price, b.stock FROM store.products a 
                               INNER JOIN store.inventories b 
                               ON a.id = b.product_id""")
                resultset = cursor.fetchall()

                for row in resultset:
                    product = Product(row[0], row[1], row[2], row[3], row[4])
                    products.append(product.to_JSON())

            connection.close()
            return products
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def create_product(self, product):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""SELECT COUNT(1) FROM products  
                                WHERE sku = %s""", (product.sku))
                row = cursor.fetchone()
                if row[0] > 0:
                    return 0

                cursor.execute("""INSERT INTO products (name, sku) 
                                VALUES (%s, %s)""", (product.name, product.sku))
                affected_rows = cursor.rowcount

                if affected_rows == 1:
                    product_id = cursor.lastrowid
                    cursor.execute("""INSERT INTO inventories (product_id, price, stock) 
                                    VALUES (%s, %s, %s)""", (product_id, product.price, product.stock))
                    affected_rows = cursor.rowcount

                connection.commit()

            connection.close()
            return 1

        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_stock(self, min_stock):
        try:
            connection = get_connection()
            products = []

            with connection.cursor() as cursor:
                cursor.execute("""SELECT a.id, a.name, a.sku, b.price, b.stock FROM store.products a 
                            INNER JOIN store.inventories b 
                            ON a.id = b.product_id
                            WHERE b.stock < %s""", (min_stock))
                resultset = cursor.fetchall()

                for row in resultset:
                    product = Product(row[0], row[1], row[2], row[3], row[4])
                    products.append(product.to_JSON())

            connection.close()
            return products

        except Exception as ex:
            raise Exception(ex)
        