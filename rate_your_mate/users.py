from flask_restful import Resource

USERS = [
    {
        "name": "Marcin Kamiński",
        "id": "8fc6734e-4765-48d9-88c2-fb9da65d52bc",
        "github": "https://github.com/marcinxkaminski",
        "linkedin": "https://www.linkedin.com/in/marcinxkaminski/",
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
    },
    {
        "name": "Adam Kowalski",
        "id": "74f9875d-400e-4508-b70a-bcb090d338fd",
        "github": "https://github.com/abc",
        "linkedin": "https://www.linkedin.com/in/abc",
        "avatar": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftranquilmonkey.com%2Fwp-content%2Fuploads%2F2016%2F05%2Fhuman-documentary.png&f=1&nofb=1",
        "room": "202",
        "city": "Cracow",
        "position": "Back-End Engineer",
        "categories": {
            "c2bb7366-e76a-42bf-a844-8596d81e158e": {
                "name": "javascript",
                "id": "c2bb7366-e76a-42bf-a844-8596d81e158e",
                "stars": 0,
            },
            "b3edb784-fa7f-4ea7-a400-b3cdc7e81651": {
                "name": "python",
                "id": "b3edb784-fa7f-4ea7-a400-b3cdc7e81651",
                "stars": 0,
            },
        },
        "badges": {},
    },
]


class Users(Resource):
    def get(self) -> str:
        """
        Gets list of users available to rate
        """
        return USERS

    def post(self) -> str:
        """
        Adds new user
        """
        json_data = request.get_json(force=True)

        return "POST"

    def put(self) -> str:
        return "PUT"

    def delete(self) -> str:
        return "DELETE"
