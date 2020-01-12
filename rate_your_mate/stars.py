from flask_restful import Resource, request
from rate_your_mate.mocks import USERS, CATEGORIES
from datetime import date

ADD_STAR_VALUE = 1


def add_star_to_user(user_id: str, category_id: str):
    USERS[user_id]["stars"] += ADD_STAR_VALUE

    if category_id in USERS[user_id]["categories"]:
        USERS[user_id]["categories"][category_id]["stars"] += ADD_STAR_VALUE
    else:
        USERS[user_id]["categories"][category_id] = {
            "id": category_id,
            "name": CATEGORIES[category_id]["name"],
            "stars": ADD_STAR_VALUE,
        }


def add_star_to_category(user_id: str, category_id: str, day: str = date.today()):
    CATEGORIES[category_id]["stars"] += ADD_STAR_VALUE

    if day in CATEGORIES[category_id]["dates"]:
        CATEGORIES[category_id]["dates"][day]["stars"] += ADD_STAR_VALUE

        if user_id in CATEGORIES[category_id]["dates"][day]["users"]:
            CATEGORIES[category_id]["dates"][day]["users"][user_id][
                "stars"
            ] += ADD_STAR_VALUE
        else:
            CATEGORIES[category_id]["dates"][day]["users"][user_id] = {
                "id": user_id,
                "stars": ADD_STAR_VALUE,
            }

    else:
        CATEGORIES[category_id]["dates"][day] = {
            "stars": ADD_STAR_VALUE,
            "users": {f"{user_id}": {"id": user_id, "stars": ADD_STAR_VALUE}},
        }


class Stars(Resource):
    def post(self) -> str:
        """
        Adds a star
        """
        stared = self.reqparse.parse_args()

        user_id = stared.get("user", {})["id"]
        category_id = stared.get("category", {})["id"]

        add_star_to_user(user_id=user_id, category_id=category_id)
        add_star_to_category(user_id=user_id, category_id=category_id)
