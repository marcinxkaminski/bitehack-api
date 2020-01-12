from flask_restful import Resource, request, reqparse
from rate_your_mate.mocks import CATEGORIES
import rate_your_mate.uuid as uuid

EMPTY_CATEGORY = {"name": "", "id": "", "stars": 0, "data": {}}


class Categories(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("user", type=dict, location="json")
        self.reqparse.add_argument("category", type=dict, location="json")
        super(Categories, self).__init__()

    def get(self) -> list:
        """
        Gets list of categories available to rate
        """
        return [{"name": c["name"], "id": c["id"]} for c_id, c in CATEGORIES.items()]

    def post(self) -> dict:
        """
        Adds new category
        """
        body = self.reqparse.parse_args()
        user = body.get("user", {})
        category = body.get("category", {})

        category_id = uuid.create()
        new_category = {**EMPTY_CATEGORY, **category, "id": category_id}
        CATEGORIES[category_id] = new_category

        return new_category

    def put(self) -> dict:
        """
        Updates category
        """
        body = self.reqparse.parse_args()

        category_id = body["category"]["id"]
        updated_category = {**CATEGORIES[category_id], **category}
        CATEGORIES[category_id] = updated_category

        return updated_category

    def delete(self):
        body = self.reqparse.parse_args()

        del CATEGORIES[body["category"]["id"]]
