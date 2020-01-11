APP_NAME = "Rate Your Mate"
API_VERSION = 1
DEBUG_MODE = True

# Endpoints
BASE_ENDPOINT = f"/api/v{API_VERSION}"
ENDPOINTS = {
    "USERS": f"{BASE_ENDPOINT}/users",
    "CATEGORIES": f"{BASE_ENDPOINT}/categories",
    "STARS": f"{BASE_ENDPOINT}/stars",
    "BADGES": f"{BASE_ENDPOINT}/badges",
    "STATS": f"{BASE_ENDPOINT}/stats",
}

# Stats
CATEGORIES_STATS_CSV_FILE_PATH = "rate_your_mate/data/categories_stats.csv"
USERS_STATS_CSV_FILE_PATH = "rate_your_mate/data/users_stats.csv"
CSV_DELIMITER = ","
CATEGORIES_CSV_HEADER = ["CATEGORY_ID", "DATE", "STARS"]
USERS_CSV_HEADER = ["USER_ID", "CATEGORY_ID", "DATE", "STARS"]

# Mocks
CATEGORIES_DATA_PATH = "rate_your_mate/data/categories-final.json"
USERS_DATA_PATH = "rate_your_mate/data/users-final.json"
