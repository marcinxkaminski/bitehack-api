from flask_restful import Resource


class Endpoint(Resource):
    def get(self) -> str:
        return "GET"

    def post(self) -> str:
        return "POST"

    def put(self) -> str:
        return "PUT"

    def delete(self) -> str:
        return "DELETE"
