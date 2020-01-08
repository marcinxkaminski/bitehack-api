from flask_restful import Api
from endpoint import Endpoint
from config import ENDPOINTS


def init_api(app) -> Api:
    if not app:
        return None

    api = Api(app)

    api.add_resource(Endpoint, ENDPOINTS.get("ENDPOINT"))

    return api
