#!/usr/bin/python

import sys
sys.stdout.flush()
from config import config
from src import init_app
from src.jobs.stock import JobStock

configuration = config['development']
app = init_app(configuration)

if __name__ == '__main__':
    JobStock.create_job()
    app.run(host='0.0.0.0', port=5000, debug=True)