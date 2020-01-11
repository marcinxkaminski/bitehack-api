from flask_restful import Api
from rate_your_mate.users import Users
from rate_your_mate.config import ENDPOINTS


def init_api(app) -> Api:
    if not app:
        return None

    api = Api(app)

    api.add_resource(Users, ENDPOINTS.get("USERS"))

    return api
