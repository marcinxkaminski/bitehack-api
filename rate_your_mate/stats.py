from flask_restful import Resource
import csv
from rate_your_mate.config import (
    CATEGORIES_STATS_CSV_FILE_PATH,
    USERS_STATS_CSV_FILE_PATH,
    CSV_DELIMITER,
    CATEGORIES_CSV_HEADER,
    USERS_CSV_HEADER,
)
from rate_your_mate.mocks import CATEGORIES


def save_data_to_csv():
    with open(CATEGORIES_STATS_CSV_FILE_PATH, "w") as categories_csv_file:
        with open(USERS_STATS_CSV_FILE_PATH, "w") as users_csv_files:
            categories_writer = csv.writer(
                categories_csv_file,
                delimiter=CSV_DELIMITER,
                quotechar='"',
                quoting=csv.QUOTE_MINIMAL,
            )
            users_writer = csv.writer(
                users_csv_files,
                delimiter=CSV_DELIMITER,
                quotechar='"',
                quoting=csv.QUOTE_MINIMAL,
            )

            categories_writer.writerow(CATEGORIES_CSV_HEADER)
            users_writer.writerow(USERS_CSV_HEADER)

            for category_id, category in CATEGORIES.items():
                for date, date_data in category["dates"].items():
                    categories_writer.writerow([category_id, date, date_data["stars"]])
                    for user_id, user in date_data["users"].items():
                        users_writer.writerow(
                            [user_id, category_id, date, user["stars"]]
                        )


class Stats(Resource):
    def get(self) -> str:
        save_data_to_csv()
        return {}
