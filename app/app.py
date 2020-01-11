from flask import Flask
from flask_cors import CORS
from api import init_api
from config import DEBUG_MODE, BASE_ENDPOINT

def main():
    app = Flask(__name__)
    cors = CORS(app, resources={rf'{BASE_ENDPOINT}/*': {"origins": "*"}})

    init_api(app=app)
    app.run(debug=DEBUG_MODE)

if __name__ == "__main__":
    main()
