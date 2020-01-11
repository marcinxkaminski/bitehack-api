from flask import Flask
from flask_cors import CORS
from rate_your_mate.api import init_api
from rate_your_mate.config import DEBUG_MODE, BASE_ENDPOINT

APP = Flask(__name__)
CORS(APP, resources={rf"{BASE_ENDPOINT}/*": {"origins": "*"}})
init_api(app=APP)

if __name__ == "__main__":
    APP.run(threaded=True, debug=DEBUG_MODE)
