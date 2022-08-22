import json
import csv


def csv_to_json(json_data):
    my_data = []
    with open("../fixtures/location.csv", encoding="utf-8") as csv_file:
        data = csv.DictReader(csv_file)

        for row in data:
            my_data.append({
                "model": "ads.location",
                "pk": row["id"],
                "fields": {
                    "name": row["name"],
                    "lat": row["lat"],
                    "lng": row["lng"],

                }
            })

    with open(json_data, "w", encoding="utf-8") as json_file:
        json_file.write(json.dumps(my_data, indent=4, ensure_ascii=False))


json_ads = r'fixtures/location.json'

csv_to_json(json_ads)


def csv_to_json(json_data):
    my_data = []
    with open("../fixtures/user.csv", encoding="utf-8") as csv_file:
        data = csv.DictReader(csv_file)

        for row in data:
            my_data.append({
                "model": "ads.user",
                "pk": row["id"],
                "fields": {
                    "first_name": row["first_name"],
                    "last_name": row["last_name"],
                    "username": row["username"],
                    "password": row["password"],
                    "role": row["role"],
                    "age": row["age"],
                    "location_id": row["location_id"],
                }
            })

    with open(json_data, "w", encoding="utf-8") as json_file:
        json_file.write(json.dumps(my_data, indent=4, ensure_ascii=False))


json_categories = r"fixtures/user.json"

csv_to_json(json_categories)
