import atexit
from src.models.ProductModel import ProductModel
from decouple import config
from apscheduler.schedulers.background import BackgroundScheduler

def stock_alert():
    try:
        min_stock = config('STOCK_MIN')

        products = ProductModel.get_stock(min_stock)
        if len(products) > 0:
            print('Productos con alerta de stock: ', products)

    except Exception as ex:
        raise Exception(ex)

scheduler = BackgroundScheduler()
scheduler.add_job(func=stock_alert, trigger="interval", seconds=5)
scheduler.start()

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())

class JobStock():
        
    @classmethod
    def create_job(self):
        try:
            stock_alert()

        except Exception as ex:
            raise Exception(ex)
        