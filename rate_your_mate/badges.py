from flask_restful import Resource
from rate_your_mate.mocks import BADGES


class Badges(Resource):
    def get(self) -> str:
        return BADGES

    def post(self) -> str:
        return "POST"

    def put(self) -> str:
        return "PUT"

    def delete(self) -> str:
        return "DELETE"
