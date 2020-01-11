from flask_restful import Api
from rate_your_mate.endpoint import Endpoint
from rate_your_mate.config import ENDPOINTS


def init_api(app) -> Api:
    if not app:
        return None

    api = Api(app)

    api.add_resource(Endpoint, ENDPOINTS.get("USERS"))

    return api
