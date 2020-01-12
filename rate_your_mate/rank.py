from flask_restful import Resource
from datetime import timedelta, date as d
from rate_your_mate.mocks import CATEGORIES, USERS
from rate_your_mate.date_helper import daterange

DAYS_IN_MONTH = 30 * 4
DAYS_IN_WEEK = 7 * 4


def get_rankings():
    today = d.today()
    date_month_ago = today - timedelta(days=DAYS_IN_MONTH)
    date_week_ago = today - timedelta(days=DAYS_IN_WEEK)

    print('month_ago:')

    monthly = {
        "users": {},
        "categories": {},
    }

    weekly = {"users": {}, "categories": {}}

    for date in daterange(start_date=date_month_ago, end_date=today):
        for category_id, category in CATEGORIES.items():
            print('dates', date, category["dates"].keys())
            if date in list(category["dates"].keys()):
                data = category["dates"]["date"]
                print('date', date)

                # Categories
                if category_id in list(monthly["categories"].keys()):
                    monthly["categories"][category_id]["stars"] += data["stars"]
                    print('1')
                else:
                    monthly["categories"][category_id] = {
                        "name": category["name"],
                        "id": category_id,
                        "stars": data["stars"],
                    }
                    print('2')

                if date >= date_week_ago:
                    if category_id in list(weekly["categories"].keys()):
                        weekly["categories"][category_id]["stars"] += data["stars"]
                        print('3')
                    else:
                        weekly["categories"][category_id] = {
                            "name": category["name"],
                            "id": category_id,
                            "stars": data["stars"],
                        }
                        print('4')

                # Users
                for user_id in list(data["users"].keys()):
                    if user_id in list(monthly["users"].keys()):
                        monthly["users"][user_id]["stars"] += data["users"][user_id][
                            "stars"
                        ]
                        print('5')
                    else:
                        monthly["users"][user_id] = {
                            "id": user_id,
                            "name": USERS[user_id]["name"],
                            "avatar": USERS[user_id]["avatar"],
                            "stars": data["users"][user_id]["stars"],
                        }
                        print('6')

                    if date >= date_week_ago:
                        if user_id in list(weekly["users"].keys()):
                            weekly["users"][user_id]["stars"] += data["users"][user_id][
                                "stars"
                            ]
                            print('7')
                        else:
                            weekly["users"][user_id] = {
                                "id": user_id,
                                "name": USERS[user_id]["name"],
                                "avatar": USERS[user_id]["avatar"],
                                "stars": data["users"][user_id]["stars"],
                            }
                            print('8')

    return {"monthly": monthly, "weekly": weekly}


class Rank(Resource):
    def get(self) -> str:
        return get_rankings()
