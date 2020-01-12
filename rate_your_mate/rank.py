from flask_restful import Resource
from rate_your_mate.mocks import CATEGORIES, USERS
from rate_your_mate.date_helper import daterange

DAYS_IN_MONTH = 30
DAYS_IN_WEEK = 7


def get_rankings():
    date_month_ago = date.today() - timedelta(days=DAYS_IN_MONTH)
    date_week_ago = date.today() - timedelta(days=DAYS_IN_WEEK)

    monthly = {
        "users": {},
        "categories": {},
    }

    weekly = {"users": {}, "categories": {}}

    for date in daterange(date_month_ago):
        for category_id, category in CATEGORIES.items():
            if date in category["dates"]:
                data = category["dates"]["date"]

                # Categories
                if category_id in monthly["categories"]:
                    monthly["categories"][category_id]["stars"] += data["stars"]
                else:
                    monthly["categories"][category_id] = {
                        "name": category["name"],
                        "id": category_id,
                        "stars": data["stars"],
                    }

                if date >= date_week_ago:
                    if category_id in weekly["categories"]:
                        weekly["categories"][category_id]["stars"] += data["stars"]
                    else:
                        weekly["categories"][category_id] = {
                            "name": category["name"],
                            "id": category_id,
                            "stars": data["stars"],
                        }

                # Users
                for user_id in list(data["users"].keys()):
                    if user_id in monthly["users"]:
                        monthly["users"][user_id]["stars"] += data["users"][user_id][
                            "stars"
                        ]
                    else:
                        monthly["u✨sers"][user_id] = {
                            "id": user_id,
                            "name": USERS[user_id]["name"],
                            "avatar": USERS[user_id]["avatar"],
                            "stars": data["users"][user_id]["stars"],
                        }

                    if date >= date_week_ago:
                        if user_id in weekly["users"]:
                            weekly["users"][user_id]["stars"] += data["users"][user_id][
                                "stars"
                            ]
                        else:
                            weekly["users"][user_id] = {
                                "id": user_id,
                                "name": USERS[user_id]["name"],
                                "avatar": USERS[user_id]["avatar"],
                                "stars": data["users"][user_id]["stars"],
                            }

    return {"monthly": monthly, "weekly": weekly}


class Rank(Resource):
    def get(self) -> str:
        return get_rankings()
