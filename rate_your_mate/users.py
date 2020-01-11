from flask_restful import Resource

USERS = [
    {
        "name": "Marcin Kamiński",
        "id": "8fc6734e-4765-48d9-88c2-fb9da65d52bc"
        "github": "https://github.com/marcinxkaminski",
        "avatar": "https://avatars2.githubusercontent.com/u/26044111?s=460&v=4",
        "room": "101",
        "city": "Cracow",
        "position": "Full Stack Engineer",
        "categories": {
            "c2bb7366-e76a-42bf-a844-8596d81e158e": {
                "name": "javascript",
                "id": "c2bb7366-e76a-42bf-a844-8596d81e158e",
                "stars": 20,
            },
            "b3edb784-fa7f-4ea7-a400-b3cdc7e81651": {
                "name": "python",
                "id": "b3edb784-fa7f-4ea7-a400-b3cdc7e81651",
                "stars": 10,
            },
        },
        "badges": {
            "c6f583ff-c062-4661-9e21-15e87e8ae0ee": {
                "id": "c6f583ff-c062-4661-9e21-15e87e8ae0ee",
                "name": "GitHub",
                "date": "2020-01-10",
                "value": 10000,
            }
        },
    }
]


class Users(Resource):
    def get(self) -> str:
        """
        Gets list of users available to rate
        """
        return USERS

    def post(self) -> str:
        return "POST"

    def put(self) -> str:
        return "PUT"

    def delete(self) -> str:
        return "DELETE"
