from flask import Flask
from api import init_api
from config import DEBUG_MODE

def main():
    app = Flask(__name__)
    init_api(app=app)
    app.run(debug=DEBUG_MODE)

if __name__ == "__main__":
    main()
