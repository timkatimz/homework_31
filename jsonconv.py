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
                    "author": row["author_id"],
                    "price": row["price"],
                    "description": row["description"],
                    "is_published": row["is_published"].title(),
                    "category": row["category_id"]
                }
            })

    with open(json_data, "w", encoding="utf-8") as json_file:
        json_file.write(json.dumps(my_data, indent=4, ensure_ascii=False))


json_ads = r'fixtures/ads.json'

csv_to_json(json_ads)


def csv_to_json(json_data):
    my_data = []
    with open("fixtures/category.csv", encoding="utf-8") as csv_file:
        data = csv.DictReader(csv_file)

        for row in data:
            my_data.append({
                "model": "ads.category",
                "pk": row["id"],
                "fields": {
                    "name": row["name"],
                    "slug": row["slug"]
                }
            })

    with open(json_data, "w", encoding="utf-8") as json_file:
        json_file.write(json.dumps(my_data, indent=4, ensure_ascii=False))


json_category = r"fixtures/category.json"

csv_to_json(json_category)


def csv_to_json(json_data):
    my_data = []
    with open("fixtures/user.csv", encoding="utf-8") as csv_file:
        data = csv.DictReader(csv_file)

        for row in data:
            my_data.append({
                "model": "users.user",
                "pk": row["id"],
                "fields": {
                    "first_name": row["first_name"],
                    "last_name": row["last_name"],
                    "username": row["username"],
                    "password": row["password"],
                    "role": row["role"],
                    "age": row["age"],
                    "birth_date": row["birth_date"],
                    "email": row["email"]
                }
            })

    with open(json_data, "w", encoding="utf-8") as json_file:
        json_file.write(json.dumps(my_data, indent=4, ensure_ascii=False))


json_user = r"fixtures/user.json"

csv_to_json(json_user)
