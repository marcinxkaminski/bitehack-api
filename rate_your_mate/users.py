from flask_restful import Resource
import rate_your_mate.uuid as uuid
from rate_your_mate.mocks import USERS

EMPTY_USER = {
    "id": "",
    "categories": {},
    "badges": {},
    "name": "",
    "github": "",
    "linkedin": "",
    "avatar": "",
    "room": "",
    "city": "",
    "position": "",
    "stars": 0,
}


class Users(Resource):
    def get(self) -> dict:
        """
        Gets list of users available to rate
        """
        return USERS

    def post(self) -> dict:
        """
        Adds new user
        """
        user = self.reqparse.parse_args()

        user_id = uuid.create()
        new_user = {**EMPTY_USER, **user, "id": user_id}
        USERS[user_id] = new_user

        return new_user

    def put(self) -> dict:
        """
        Updates user
        """
        user = self.reqparse.parse_args()

        user_id = user["id"]
        updated_user = {**USERS[user_id], **user}
        USERS[user_id] = updated_user

        return updated_user

    def delete(self):
        user = self.reqparse.parse_args()

        del USERS[user["id"]]
