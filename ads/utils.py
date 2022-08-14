import json
import csv


def csv_to_json(json_data):
    my_data = []
    with open("fixtures/ads.csv", encoding="utf-8") as csv_file:
        data = csv.DictReader(csv_file)

        for row in data:
            my_data.append({
                "model": "ads.ads",
                "pk": row["id"],
                "fields": {
                    "name": row["name"],
                    "author": row["author"],
                    "price": row["price"],
                    "description": row["description"],
                    "address": row["address"],
                    "is_published": row["is_published"].title()
                }
            })

    with open(json_data, "w", encoding="utf-8") as json_file:
        json_file.write(json.dumps(my_data, indent=4, ensure_ascii=False))


json_ads = r'fixtures/ads.json'

csv_to_json(json_ads)


def csv_to_json(json_data):
    my_data = []
    with open("fixtures/categories.csv", encoding="utf-8") as csv_file:
        data = csv.DictReader(csv_file)

        for row in data:
            my_data.append({
                "model": "ads.category",
                "pk": row["id"],
                "fields": {
                    "name": row["name"],
                }
            })

    with open(json_data, "w", encoding="utf-8") as json_file:
        json_file.write(json.dumps(my_data, indent=4, ensure_ascii=False))


json_categories = r"fixtures/category.json"

csv_to_json(json_categories)
