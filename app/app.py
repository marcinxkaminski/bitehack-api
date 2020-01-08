from flask import Flask
from api import init_api
from config import DEBUG_MODE

APP = Flask(__name__)

init_api(app=APP)

if __name__ == "__main__":
    APP.run(debug=DEBUG_MODE)
