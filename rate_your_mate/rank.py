from flask_restful import Resource
from datetime import timedelta, date as d
from rate_your_mate.mocks import CATEGORIES, USERS
from rate_your_mate.date_helper import daterange

DAYS_IN_MONTH = 30
DAYS_IN_WEEK = 7 * 2


def get_rankings():
    today = d.today()
    date_month_ago = today - timedelta(days=DAYS_IN_MONTH)
    date_week_ago = today - timedelta(days=DAYS_IN_WEEK)

    monthly = {
        "users": {},
        "categories": {},
    }

    weekly = {"users": {}, "categories": {}}

    for day_date in daterange(start_date=date_month_ago, end_date=today):
        day = str(day_date)
        for category_id, category in CATEGORIES.items():
            if str(day) in list(category["dates"].keys()):
                data = category["dates"][day]

                # Categories
                if category_id in list(monthly["categories"].keys()):
                    monthly["categories"][category_id]["stars"] += data["stars"]
                else:
                    monthly["categories"][category_id] = {
                        "name": category["name"],
                        "id": category_id,
                        "stars": data["stars"],
                    }

                if day_date >= date_week_ago:
                    if category_id in list(weekly["categories"].keys()):
                        weekly["categories"][category_id]["stars"] += data["stars"]
                    else:
                        weekly["categories"][category_id] = {
                            "name": category["name"],
                            "id": category_id,
                            "stars": data["stars"],
                        }

                # Users
                for user_id in list(data["users"].keys()):
                    if user_id in list(monthly["users"].keys()):
                        monthly["users"][user_id]["stars"] += data["users"][user_id][
                            "stars"
                        ]
                    else:
                        monthly["users"][user_id] = {
                            "id": user_id,
                            "name": USERS[user_id]["name"],
                            "avatar": USERS[user_id]["avatar"],
                            "stars": data["users"][user_id]["stars"],
                        }

                    if day_date >= date_week_ago:
                        if user_id in list(weekly["users"].keys()):
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
