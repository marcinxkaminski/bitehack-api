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
}
