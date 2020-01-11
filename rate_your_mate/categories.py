from flask_restful import Resource

CATEGORIES = [
    {
        "name": "javascript",
        "id": "c2bb7366-e76a-42bf-a844-8596d81e158e",
        "stars": 20,
        "data": {
            "2020-01-10": {
                "stars": 8,
                "users": [{"id": "8fc6734e-4765-48d9-88c2-fb9da65d52bc", "stars": 8}],
            },
            "2020-01-11": {
                "stars": 12,
                "users": [{"id": "8fc6734e-4765-48d9-88c2-fb9da65d52bc", "stars": 12}],
            },
        },
    },
    {
        "name": "python",
        "id": "b3edb784-fa7f-4ea7-a400-b3cdc7e81651",
        "stars": 10,
        "data": {
            "2020-01-10": {
                "stars": 2,
                "users": [{"id": "8fc6734e-4765-48d9-88c2-fb9da65d52bc", "stars": 2}],
            },
            "2020-01-11": {
                "stars": 8,
                "users": [{"id": "8fc6734e-4765-48d9-88c2-fb9da65d52bc", "stars": 8}],
            },
        },
    },
]


class Categories(Resource):
    def get(self) -> str:
        """
        Gets list of categories available to rate
        """
        return [{"name": c["name"], "id": c["id"]} for c in CATEGORIES]

    def post(self) -> str:
        return "POST"

    def put(self) -> str:
        return "PUT"

    def delete(self) -> str:
        return "DELETE"
