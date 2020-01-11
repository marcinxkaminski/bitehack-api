from rate_your_mate.config import CATEGORIES_DATA_PATH, USERS_DATA_PATH
import json


def load_data(file: str) -> dict:
    with open(file, "r") as f:
        return json.load(f)


USERS = load_data(file=USERS_DATA_PATH)

CATEGORIES = load_data(file=CATEGORIES_DATA_PATH)

BADGES = {}
