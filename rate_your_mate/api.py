from flask_restful import Api
from rate_your_mate.users import Users
from rate_your_mate.stars import Stars
from rate_your_mate.badges import Badges
from rate_your_mate.categories import Categories
from rate_your_mate.stats import Stats
from rate_your_mate.config import ENDPOINTS


def init_api(app):
    if not app:
        return

    api = Api(app)

    api.add_resource(Users, ENDPOINTS["USERS"])
    api.add_resource(Categories, ENDPOINTS["CATEGORIES"])
    api.add_resource(Stars, ENDPOINTS["STARS"])
    api.add_resource(Badges, ENDPOINTS["BADGES"])
    api.add_resource(Stats, ENDPOINTS["STATS"])
