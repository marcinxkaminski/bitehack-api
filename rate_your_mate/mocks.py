from rate_your_mate.config import CATEGORIES_DATA_PATH, USERS_DATA_PATH
import json


def load_data(file: str) -> dict:
    with open(file, "r") as f:
        return json.load(f)

def save_data(file: str, data: dict):
    with open(file, "w") as f:
        return json.dump(data, file)

def save_users(users: dict):
    save_data(file=USERS_DATA_PATH, data=users)

def save_categories(categories: dict):
    save_data(file=CATEGORIES_DATA_PATH, data=categories)


USERS = load_data(file=USERS_DATA_PATH)

CATEGORIES = load_data(file=CATEGORIES_DATA_PATH)

BADGES = {}
