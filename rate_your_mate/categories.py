from flask_restful import Resource
from rate_your_mate.mocks import CATEGORIES
import rate_your_mate.uuid as uuid

EMPTY_CATEGORY = {"name": "", "id": "", "stars": 0, "data": {}}


class Categories(Resource):
    def get(self) -> list:
        """
        Gets list of categories available to rate
        """
        return [{"name": c["name"], "id": c["id"]} for c in CATEGORIES]

    def post(self) -> dict:
        """
        Adds new category
        """
        body = request.get_json(force=True)
        user = body.get("user", {})
        category = body.get("category", {})

        id = uuid.create()
        new_category = {**EMPTY_CATEGORY, **category, "id": id}
        CATEGORIES[id] = new_category

        return new_category

    def put(self) -> dict:
        """
        Updates category
        """
        category = request.get_json(force=True)

        id = category["id"]
        updated_category = {**CATEGORIES[id], **category}
        CATEGORIES[id] = updated_category

        return updated_category

    def delete(self):
        category = request.get_json(force=True)

        del CATEGORIES[category["id"]]
