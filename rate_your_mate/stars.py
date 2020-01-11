from flask_restful import Resource
from rate_your_mate.mocks import USERS, CATEGORIES

def add_star_to_user(user_id: str, category_id: str):
    user = USERS[user_id]

    user["stars"] += 1

    if category_id in user["categories"]:
        user["categories"][category_id]["stars"] += 1
    else:
        pass


def add_star_to_category():
    pass

class Stars(Resource):
    def post(self) -> str:
        """
        Adds a star
        """
        stared = request.get_json(force=True)

        user_id = stared.get("user", {})["id"]
        category_id = stared.get("category", {})["id"]
