from resources.web_server import *

from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)


import logging
import os

api.add_resource(WebService, '/santander') # HTTP GET to print Santander String

if __name__ == '__main__':
    logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
    log = logging.getLogger(__name__)

    app.run(host="0.0.0.0", port=int("5004"), debug=True)